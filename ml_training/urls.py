from django.conf.urls import include, url
from snippets import simple_i18n_patterns as i18n_patterns
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('competition.urls', namespace='competition')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500
