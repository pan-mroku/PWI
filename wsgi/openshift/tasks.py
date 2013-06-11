from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery import task, current_task
from celery.result import AsyncResult
from time import sleep
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404, redirect
from testy.models import StringTest
jobs=[]

@task()
def do_work():
    for i in range(100):
        sleep(0.1)
        current_task.update_state(state='PROGRESS', meta={'current': i})
    return {'current':100}

@task()
def check_howmanystrings(stringValue):
    current_task.update_state(state='PROGRESS', meta={'current': "working"})
    numberofstrings=0
    try:
        numberofstrings=len(StringTest.objects.filter(value=str(stringValue)))
    except (StringTest.DoesNotExist,TypeError):
        numberofstrings=0
    print 'job value = '+str(numberofstrings)
    return {'value':numberofstrings}

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
def init_stringwork(value):
    stringvalue = value
    job = check_howmanystrings.delay(stringvalue)
    print 'append new job, id= '+job.id
    jobs.append(job.id)
    return job.id

def init_work(request):
    """ A view to start a background job and redirect to the status page """
    if 'stringval' not in request.GET:
        return HttpResponse('No string value given.')
    stringvalue = request.GET['stringval']
    job = check_howmanystrings(stringvalue)
    jobs.append(job.id)
    return redirect(reverse('home'))

def delete_job(request):
    if 'job' not in request.GET:
        return HttpResponse('No job id given.')
    job_id = request.GET['job']
    job=AsyncResult(job_id)
    jobs.remove(job)
    return redirect(reverse('home'))
        

#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def clean_works():
#    for job in jobs:
#        if job.state=='SUCCESS':
#            jobs.remove(job)
