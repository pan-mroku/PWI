import os
import socket
from celery.result import AsyncResult
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
#from openshift.tasks import *
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wsgi.openshift.couchdb_methods import *
from tasks import append_message

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

def login(request):
    username = request.POST['login']
    request.session['user']= username
    SERVER = Server('http://194.29.175.241:5984/')
    chat= SERVER['chat']
    if username in chat: #zakladam ze id == username, co ma sens skoro to unikalne wpisy
        user = chat[username]
        user['active'] = True
    else:
        chat[username] = {'active': True, 'host': socket.gethostname(), 'delivery':"tttttttttttttttttteeest"} #Trzeba bedzie na OS sprawdzic jak sie rejestruje
    return redirect(reverse('home'))

@login_required
def add_message(request):
    user=request.user
    message=Message(uuid=uuid4(), user=user, message=request.POST['message'], timestamp=timezone.now())
    message.save()
    append_message(message)
    return redirect(reverse('home'))

#dla szybkiego sprawdzenia czy couchdb stoi i jak z danymi na ktorych operujemy.
#by sprawdzic main bazy danych, czyli same dokumenty, zrobic iteracje po SERVER (bez arg)
def couchdb_browser(request):
    return render(request, 'couchdb_browser.html',{'docs': get_chatData(True), 'chat':True}) #jezeli przegladam sobie dokument chat to true

