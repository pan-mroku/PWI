from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from models import StringTest
from django.http import HttpResponse, HttpResponseRedirect


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