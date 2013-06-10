from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_task/', 'openshift.tasks.init_work', name='add_task'),
    url(r'^task/','openshift.views.task', name='task'),
    url(r'^delete_task/','openshift.tasks.delete_job',name='delete_task'),
    #url(r'poll_state/', 'openshift.tasks.poll_state', name="poll_state")
)
