from django import template

register = template.Library()

@register.inclusion_tag('search/search_form.html')
def show_seach_form():
    return { }
