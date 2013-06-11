import os
from django.shortcuts import render_to_response

def home(request):
    choice_list = ['admin','polls','testy','chat']
    return render_to_response('home/home.html',{'choices_list':choice_list})
