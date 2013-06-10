from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home
admin.autodiscover()
urlpatterns = patterns('',
url(r'^$','openshift.views.home'),
url(r'^polls/', include('polls.urls')),
url(r'^testy/', include('testy.urls')),
url(r'^admin/', include(admin.site.urls)),
)