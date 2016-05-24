from django.conf.urls import include, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = [
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('competition.urls', namespace='competition')),
    url(r'^admin/', include(admin.site.urls)),
]

# urlpatterns += i18n_patterns()

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500
