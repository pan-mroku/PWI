from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery import task, current_task
from celery.result import AsyncResult
from time import sleep
from couchdb import Server
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404, redirect
from couchdb_methods import get_chatData
from settings import HOST_NAME
import requests
from models import Message
from django.views.decorators.csrf import csrf_exempt

jobs=[]

@task
def do_work():
    for i in range(100):
        sleep(0.1)
        current_task.update_state(state='PROGRESS', meta={'current': i})
    return {'current':100}

#def poll_state(request):
#    """ A view to report the progress to the user """
#    if 'job' in request.GET:
#        job_id = request.GET['job']
#    else:
#        return HttpResponse('No job id given.')
#
#    job = AsyncResult(job_id)
#    data = job.result or job.state
#    return HttpResponse(json.dumps(data), mimetype='application/json')

def init_work(request):
    """ A view to start a background job and redirect to the status page """
    job = do_work.delay()
    print job.id
    jobs.append(job.id)
    return redirect(reverse('home'))

def delete_job(request):
    if 'job' not in request.GET:
        return redirect(reverse('home'))
    job_id = request.GET['job']
    jobs.remove(job_id)
    return redirect(reverse('home'))


#metody z egzaminu - chat

@task()
def send_message(message):
    chatdata=get_chatData(True)
    urilist=[]
    for user in chatdata:
        if user['host'][0:4] == "http" and user['delivery'][0:4] != "http":
            if HOST_NAME != user['host']: #ignorujemy swoj hostname, by sie wiadomosci nie zdublowaly
                urilist.append(user['host']+user['delivery'])
    length = len(urilist)
    print "urilist length = "+str(length)
    i=0
    if length>0:
        for uri in urilist:
            print "Sending message (["+str(message["timestamp"])+"] "+message['user']+": "+message['message']+") \r\n to: "+uri
            requests.post(uri,message) #zakladam ze message juz jest w postaci json
            i=i+100/length
            current_task.update_state(state='PROGRESS', meta={'current': i})
    return {'current':100}


@csrf_exempt
def get_message(request):
    create_and_save_message.delay(request.POST)
    return HttpResponse()

@task()
def create_and_save_message(json):
    message=Message()
    message.json_decode(json)
    message.save()

@task()
def register_to_couchdb():
    id = HOST_NAME
    SERVER = Server('http://194.29.175.241:5984/')
    chat= SERVER['chat']
    if id in chat: #zakladam ze id == username, co ma sens skoro to unikalne wpisy
        user = chat[id]
        user['active'] = True
    else:
        chat[id] = {'active': True, 'host': HOST_NAME, 'delivery':"get_message/"} #Trzeba bedzie na OS sprawdzic jak sie rejestruje
    return

#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def clean_works():
#    for job in jobs:
#        if job.state=='SUCCESS':
#            jobs.remove(job)
