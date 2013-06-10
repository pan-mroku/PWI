from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^add_task/', 'openshift.tasks.init_work', name='add_task'),
    url(r'^task/','openshift.views.task', name='task'),
    url(r'^delete_task/','openshift.tasks.delete_job',name='delete_task'),

    url(r'^admin/', include(admin.site.urls)),
)
