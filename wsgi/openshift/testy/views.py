from datetime import datetime
from time import sleep
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader, RequestContext
from models import StringTest
from django.http import HttpResponse, HttpResponseRedirect
from openshift.tasks import *


def index(request):
    latest_poll_list = StringTest.objects.all().order_by("-pub_date")[:5]
    return render_to_response("testy/index.html", {"latest_list": latest_poll_list})


def add(request):
    try:
        text = request.POST["text"]
        newString = StringTest(value=text, pub_date=datetime.now())
        newString.save()
        return HttpResponseRedirect(reverse("testy.views.index"))
    except (KeyError):
        # Redisplay the form.
        return render_to_response("testy/add.html", context_instance=RequestContext(request))

def check(request):
    try:
        text = request.POST["text"]
        id = init_stringwork(text) #odwolywanie sie do tasks.init_stringwork(text)
        return redirect('testy.views.checkjob', job_id=id)
        #return render_to_response("testy/checkjob.html", {"job_id": str(id)}) #bo mi redirect nie dziala, a jest juz po polnocy :/
    except (KeyError):
        # Redisplay the form.
        return render_to_response("testy/check.html", context_instance=RequestContext(request))

def checkjob(request, job_id):
    job = AsyncResult(job_id)
    data = '<b>Nie ma jeszcze wynikow, strona powinna sie odswiezyc za 2 sek, jesli tak sie nie stalo, to kliknij <a href="">TU</a>.</b>'
    if isinstance(job.result, dict):
        data = "Liczba wynikow: "+ str(job.result['value'])

    return render_to_response("testy/checkjob.html", {"job": data, "job_id":job_id})