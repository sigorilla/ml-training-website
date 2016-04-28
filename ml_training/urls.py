from django.conf.urls import include, url

from django.contrib import admin
from django.views.generic import TemplateView

import views

admin.autodiscover()

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='index.html')),
    url(r'^', include('event.urls', namespace='event')),
    url(r'^admin/', include(admin.site.urls)),
]

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500
