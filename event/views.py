# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.views import generic

import re

from models import Event


class SearchMixin(object):

    @staticmethod
    def normalize_query(query_string,
                        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                        normspace=re.compile(r'\s{2,}').sub):
        return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

    def get_query(self, query_string, search_fields):
        # Query to search for every search term
        query = None
        terms = self.normalize_query(query_string)
        for term in terms:
            # Query to search for a given term in each field
            or_query = None
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query | or_query
        return query


class NeverCacheMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(NeverCacheMixin, cls).as_view(**initkwargs)
        return never_cache(view)


class EventListView(NeverCacheMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    paginate_by = 20

    def get_queryset(self):
        queryset = super(EventListView, self).get_queryset()
        return queryset.filter(active__exact=True)


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


class SearchEventListView(SearchMixin, NeverCacheMixin, generic.ListView):
    model = Event
    template_name = 'event/search_event.html'
    context_object_name = 'events'

    def get_queryset(self):
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            query_string = self.request.GET['q'].strip()
            entry_query = self.get_query(query_string, ['title', 'content'])
            return Event.objects.filter(entry_query).order_by('-pub_date')
        else:
            return Event.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            self.template_name = 'event/search_event_ajax.html'
        return super(SearchEventListView, self).render_to_response(
            context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchEventListView, self).get_context_data(**kwargs)
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            context['query'] = self.request.GET['q'].strip()
            context['title'] = self.request.GET['q'].strip()
        else:
            context['query'] = ''
            context['title'] = 'Поиск'
        return context