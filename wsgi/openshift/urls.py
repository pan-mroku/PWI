from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home
admin.autodiscover()
urlpatterns = patterns('',
url(r'^$','openshift.views.home', name='home'),
url(r'^polls/', include('polls.urls'), name='polls'),
url(r'^testy/', include('testy.urls'), name='testy'),
url(r'^admin/', include(admin.site.urls), name='admin'),
url(r'^chat/', include('chat.urls'), name='chat'),
)