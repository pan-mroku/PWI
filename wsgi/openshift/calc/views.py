import os
import socket
from celery.result import AsyncResult
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
import requests
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from couchdb_methods import *

def home(request):
    lines=Message.objects.all().order_by('-timestamp')
    return render(request,'home.html',{'lines':lines,})

def home_redirect(request):
    return redirect(reverse('home'))

def task(request):
    if 'job' not in request.GET:
        return redirect(reverse('home'))
    job_id = request.GET['job']
    job = AsyncResult(job_id)
    data = job.result or job.state
    return render(request, 'echo.html',{'what':json.dumps(data),'job':job_id,})

#dla szybkiego sprawdzenia czy couchdb stoi i jak z danymi na ktorych operujemy.
#by sprawdzic main bazy danych, czyli same dokumenty, to trzeba zrobic iteracje po SERVER (bez arg)
def couchdb_browser(request):
    return render(request, 'couchdb_browser.html',{'docs': get_calcData(True), 'chat':True}) #jezeli przegladam sobie dokument chat to true

def compute(request):
    if 'calc' not in request.GET:
        return redirect(reverse('home'))
    