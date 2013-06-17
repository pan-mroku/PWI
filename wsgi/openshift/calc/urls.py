from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'calc.views.home', name='home'),
    url(r'^add_task/', 'calc.tasks.init_work', name='add_task'),
    url(r'^task/','calc.views.task', name='task'),
    url(r'^delete_task/','calc.tasks.delete_job',name='delete_task'),
    url(r'^couchdb_browser/','calc.views.couchdb_browser'),
    url(r'^add_calc', 'chat.views.compute', name='add_calc'),

)
