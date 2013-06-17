from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    apps={}
    apps['chat']="/chat/"
    return render(request, 'index.html',{'apps':apps})

def index_redirect(request):
    return redirect(reverse('index'))
