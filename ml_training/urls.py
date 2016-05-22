from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('competition:index'))),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('competition.urls', namespace='competition')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500
