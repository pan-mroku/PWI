from django.conf.urls import patterns, include, url


urlpatterns = patterns("",
url(r"^$","chat.views.home", name="home"),
url(r"^room/$","chat.views.room", name="room"),


)
