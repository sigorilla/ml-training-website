from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CompetitionListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CompetitionDetailView.as_view(), name='detail'),
    url(r'^search/$', views.SearchCompetitionListView.as_view(), name='search'),
]
