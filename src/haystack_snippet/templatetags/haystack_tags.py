from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

from haystack_snippet.forms import HaystackSearchForm
from haystack_snippet.views import DEFAULT_PREFIX

@register.inclusion_tag('search/search_form.html')
def show_search_form(request, place_holder=_('Search')):
    return { 
        'search_form': HaystackSearchForm(request.GET or None, prefix=DEFAULT_PREFIX),
        'place_holder': place_holder,
    }
