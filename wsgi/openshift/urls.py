from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'openshift.views.index', name='index'),
    url(r'^chat/', include('chat.urls')),
    url(r'^calc/', include('calc.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'accounts/register/complete/', 'chat.views.home_redirect'),
    #url(r'login/', 'django.contrib.auth.views.login'),
    #url(r'logout/', 'django.contrib.auth.views.logout',{'next_page':'/'}),
    #url(r'accounts/', include('registration.backends.simple.urls')),

    #url(r'users/','openshift.views.index_redirect'),

    url(r'login/','openshift.views.login_user'),
    url(r'logout/','openshift.views.logout_user'),
)
