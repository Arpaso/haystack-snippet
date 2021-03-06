### -*- coding: utf-8 -*- ####################################################

from datetime import timedelta, datetime, date

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import F
from django.conf import settings
from django.utils.encoding import force_unicode

from pytils.translit import detranslify, translify
from haystack.views import SearchView
from haystack.query import RelatedSearchQuerySet, SearchQuerySet, SQ

from .utils import replace_special
from .models import SearchLogger
from .forms import HaystackSearchForm

DETRANSLIFY_SEARCH_QUERY = getattr(settings, 'DETRANSLIFY_SEARCH_QUERY', True)
DEFAULT_PREFIX = getattr(settings, 'DEFAULT_SEARCH_PREFIX', 'search')


class HaystackSearchView(SearchView):
    
    detranslify = DETRANSLIFY_SEARCH_QUERY
    searchqueryset = SearchQuerySet
    
    def __init__(self, template=None, load_all=True, form_class=None, context_class=RequestContext, results_per_page=None):
        self.load_all = load_all
        self.form_class = form_class
        self.context_class = context_class
        
        if form_class is None:
            self.form_class = HaystackSearchForm
        
        if not results_per_page is None:
            self.results_per_page = results_per_page
        
        if template:
            self.template = template
    
    def get_results(self):
        """
        Fetches the results via the form.

        Returns an empty list if there's no query to search with.
        """
        query = self.query

        if not (self.form.is_valid() and query):
            return self.form.no_query_found()

        #Replace letter ё --> е
        query = replace_special(query)

        # save the query to statistic
        if 'page' not in self.request.GET and query:
            rows = SearchLogger.objects.filter(text=query).update(counter=F('counter')+1)
            if not rows:
                SearchLogger.objects.create(text=query)
        
        translited_query = force_unicode(translify(query))
        detranslited_query = force_unicode(detranslify(query))
        
        sqs = self.searchqueryset().filter_and(SQ(content=detranslited_query) | SQ(content=translited_query) | SQ(content=query))
        
        #sqs = self.searchqueryset().auto_query(query)
        
        if self.load_all:
            sqs = sqs.load_all()
        
        return sqs

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        
        context = {
            'object_list': self.results,
            'search_term': self.query,
        }

        context.update(self.extra_context())

        return render_to_response(self.template, context, context_instance=self.context_class(self.request))

    def extra_context(self):
        """
        Allows the addition of more context variables as needed.

        Must return a dictionary.
        """
        return self._extra_context or {}

    def __call__(self, request, template_name=None, extra_context=None):
        """
        Generates the actual response to the search.

        Relies on internal, overridable methods to construct the response.
        """
        self._extra_context = extra_context
        if template_name:
            self.template = template_name

        return super(HaystackSearchView, self).__call__(request)

    def build_form(self, form_kwargs=None):
        """
        Instantiates the form the class should use to process the search query.
        """
        data = None
        kwargs = {
            'load_all': self.load_all,
            'prefix': DEFAULT_PREFIX
        }
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.GET):
            data = self.request.GET

        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = self.searchqueryset
        
        return self.form_class(data=data, **kwargs)
