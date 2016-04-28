# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import Resolver404
from django.views.decorators.cache import never_cache
from django.views import generic

from models import Event


class NeverCacheMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(NeverCacheMixin, cls).as_view(**initkwargs)
        return never_cache(view)


class EventListView(NeverCacheMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    # TODO: add pagination
    # paginate_by = 20

    def get(self, request, *args, **kwargs):
        content = super(EventListView, self).get(request, *args, **kwargs)
        if self.object_list.count() == 0:
            raise Resolver404
        return content


class EventDetailView(NeverCacheMixin, generic.DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        content = super(EventDetailView, self).get(request, *args, **kwargs)
        if not (request.user.is_staff or self.object.active):
            raise PermissionDenied
        return content

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_staff or self.object.active:
            context['title'] = self.get_object().title
        return context
