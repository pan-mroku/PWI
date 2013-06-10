from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from models import Poll, Choice

urlpatterns = patterns("",
url(r"^$",
ListView.as_view(
queryset=Poll.objects.order_by("-pub_date")[:5],
context_object_name="latest_poll_list",
template_name="polls/index.html")),

url(r"^(?P<pk>\d+)/$",
DetailView.as_view(
model=Poll,
template_name="polls/detail.html")),

url(r"^(?P<poll_id>\d+)/results/$",  "polls.views.results"), #nie mozna robic redirectow na generic view napisany tak jak wyzej

url(r"^(?P<poll_id>\d+)/vote/$", "polls.views.vote"),)