import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from openshift.tasks import *

def home(request):
    global jobs
    return render(request,'home.html',{'jobs':jobs})

def task(request):
    if 'job' not in request.GET:
        return redirect(reverse('home'))
    job_id = request.GET['job']
    job = AsyncResult(job_id)
    data = job.result or job.state
    return render(request, 'echo.html',{'what':json.dumps(data),'job':job_id,})
