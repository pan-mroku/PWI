from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from models import StringTest

urlpatterns = patterns("",
url(r"^$","testy.views.index"),

url(r"^(?P<pk>\d+)/$",
DetailView.as_view(
model=StringTest,
context_object_name="StringTest",
template_name="testy/detail.html")),

url(r"^add/", "testy.views.add"),)