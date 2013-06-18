from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

users=[]

def index(request):
    apps={}
    apps['chat']="/chat/"
    apps['calc']="/calc/"
    return render(request, 'index.html',{'apps':apps})

def index_redirect(request):
    return redirect(reverse('index'))

def login_user(request):
    if request.method=='POST':
        user=request.POST['login']
        if user in users:
            return redirect(reverse('chat_home'))
        users.append(user)
        request.session['user']=request.POST['login']
        return redirect(reverse('chat_home'))

def logout_user(request):
    if 'user' not in request.session:
        return redirect(reverse('chat_home'))
    user=request.session['user']
    users.remove(user)
    del request.session['user']
    return redirect(reverse('chat_home'))
