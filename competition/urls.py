from django.conf.urls import url
from . import views
from feeds import RssCompetitionsFeed, AtomCompetitionsFeed

urlpatterns = [
    url(r'^$', views.CompetitionListView.as_view(), name='index'),
    url(r'^rss/$', RssCompetitionsFeed(), name='rss'),
    url(r'^atom/$', AtomCompetitionsFeed(), name='atom'),
    url(r'^(?P<pk>\d+)/$', views.detail_redirect, name='detail'),
    url(r'^search/$', views.SearchCompetitionListView.as_view(), name='search'),
    url(r'^new/$', views.CreateCompetitionView.as_view(), name='create')
]
