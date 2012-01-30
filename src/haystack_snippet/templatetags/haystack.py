from django import template

register = template.Library()

from haystack_snippet.forms import HaystackSearchForm

@register.inclusion_tag('search/search_form.html')
def show_search_form(request):
    form = HaystackSearchForm(request.GET or None, prefix="search")
    print form
    return { "search_form": form }
