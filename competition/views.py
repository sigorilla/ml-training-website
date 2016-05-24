from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.views import generic
from django.utils.translation import ugettext as _

import re

from models import Competition


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


class FilterListMixin(generic.ListView):

    def get_context_data(self, **kwargs):
        context = super(FilterListMixin, self).get_context_data(**kwargs)
        filter_by = self.request.GET[settings.FILTER_KEY].strip() \
            if settings.FILTER_KEY in self.request.GET else 'active'
        if filter_by not in ['active', 'finished', 'all']:
            filter_by = 'active'
        active_queryset = []
        finished_queryset = []
        if filter_by == 'active' or filter_by == 'all':
            active_queryset = self.get_queryset().filter(finish_date__gte=timezone.now()).order_by('finish_date')
        if filter_by == 'finished' or filter_by == 'all':
            finished_queryset = self.get_queryset().filter(finish_date__lte=timezone.now()).order_by('-finish_date')

        queryset = list(active_queryset) + list(finished_queryset)
        if len(queryset):
            context[self.context_object_name] = queryset

        context['filter'] = filter_by
        return context


class CompetitionListView(NeverCacheMixin, FilterListMixin):
    model = Competition
    context_object_name = 'competitions'
    paginate_by = 20

    def get_queryset(self):
        queryset = super(CompetitionListView, self).get_queryset()
        return queryset.filter(active__exact=True)


class CompetitionDetailView(NeverCacheMixin, generic.DetailView):
    model = Competition

    def get(self, request, *args, **kwargs):
        content = super(CompetitionDetailView, self).get(request, *args, **kwargs)
        if not (request.user.is_staff or self.object.active):
            raise PermissionDenied
        return content

    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_staff or self.object.active:
            context['title'] = self.get_object().title
        return context


class SearchCompetitionListView(SearchMixin, NeverCacheMixin, FilterListMixin):
    model = Competition
    template_name = 'competition/search_competition.html'
    context_object_name = 'competitions'

    def get_queryset(self):
        queryset = Competition.objects.all()
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            query_string = self.request.GET['q'].strip()
            entry_query = self.get_query(query_string, ['title', 'content'])
            queryset = queryset.filter(entry_query)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            self.template_name = 'competition/search_competition_ajax.html'
        return super(SearchCompetitionListView, self).render_to_response(
            context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchCompetitionListView, self).get_context_data(**kwargs)
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            context['query'] = self.request.GET['q'].strip()
            context['title'] = self.request.GET['q'].strip()
        else:
            context['query'] = ''
            context['title'] = _('Search')
        return context


def detail_redirect(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    return HttpResponseRedirect(competition.link)
