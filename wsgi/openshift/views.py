import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
#from openshift.tasks import *
from openshift.models import *
from django.contrib.auth.models import User

def home(request):
    lines=Message.objects.all().order_by('-timestamp')
    user=request.session.get('user')
    return render(request,'home.html',{'lines':lines,'user':user})

def task(request):
    if 'job' not in request.GET:
        return redirect(reverse('home'))
    job_id = request.GET['job']
    job = AsyncResult(job_id)
    data = job.result or job.state
    return render(request, 'echo.html',{'what':json.dumps(data),'job':job_id,})

def login(request):
    request.session['user']=request.POST['login']
    return redirect(reverse('home'))

def add_message(request):
    user=request.session.get('user')
    message=Message(uuid=uuid4(), user=user, message=request.POST['message'], timestamp=timezone.now())
    print message
    message.save()
    return redirect(reverse('home'))
                    
