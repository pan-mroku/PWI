from datetime import datetime
import socket
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader, RequestContext
from models import User, Message


def home(request):
     try:
        nicknm = request.POST["username"]
        try:
            HOSTNAME = socket.gethostname()
        except:
            HOSTNAME = 'localhost'
        userfilter=User.objects.filter(nickname=str(nicknm))
        if len(userfilter)>0:
            user=userfilter[0]
        else:
            user = User(nickname=nicknm, ip=HOSTNAME, create_date=datetime.now())
            user.save()
        #User.objects.all().delete()

        request.session['usrname'] = nicknm
        return redirect(room)

     except (KeyError):
        return render_to_response("chat/home.html", context_instance=RequestContext(request))

def room(request):
    try:
        nickname=request.session['usrname']
    except (KeyError):
        nickname="Guest"

    messages=Message.objects.all()
    try:

        msg = request.POST["message"]
        message = Message(user=User.objects.get(nickname=nickname),message=msg,timestamp = datetime.now())
        message.save()
        messages=Message.objects.all()
        return render_to_response("chat/room.html", {'username': nickname, 'messages':messages }, context_instance=RequestContext(request))
    except (KeyError):
        return render_to_response("chat/room.html", {'username': nickname, 'messages':messages}, context_instance=RequestContext(request))
