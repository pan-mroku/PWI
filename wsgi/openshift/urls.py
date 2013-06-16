from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^add_task/', 'openshift.tasks.init_work', name='add_task'),
    url(r'^task/','openshift.views.task', name='task'),
    url(r'^delete_task/','openshift.tasks.delete_job',name='delete_task'),
    
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^add_message', 'openshift.views.add_message', name='add_message'),
    url(r'accounts/register/complete/', 'openshift.views.home_redirect'),
    url(r'^accounts/', include('registration.backends.simple.urls'),{'success_url':'/'}),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^users/','openshift.views.home_redirect'),
    #Test CouchDB - pokazuje dane z CDB
    url(r'^couchdb_browser/','openshift.views.couchdb_browser'),
    url(r'^get_message/','openshift.tasks.get_message',)

)
