from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'chat.views.home', name='home'),
    url(r'^add_task/', 'chat.tasks.init_work', name='add_task'),
    url(r'^task/','chat.views.task', name='task'),
    url(r'^delete_task/','chat.tasks.delete_job',name='delete_task'),
    
    url(r'^add_message', 'chat.views.add_message', name='add_message'),
    url(r'accounts/register/complete/', 'chat.views.home_redirect'),
    url(r'^accounts/', include('registration.backends.simple.urls'),{'success_url':'/chat/'}),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'/chat/'}, name='logout'),
    url(r'^users/','chat.views.home_redirect'),
    #Test CouchDB - pokazuje dane z CDB
    url(r'^couchdb_browser/','chat.views.couchdb_browser'),
    url(r'^get_message/','chat.tasks.get_message',)

)
