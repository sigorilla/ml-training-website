from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^search/$', views.SearchEventListView.as_view(), name='search'),
]
