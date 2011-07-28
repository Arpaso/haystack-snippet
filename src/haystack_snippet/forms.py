### -*- coding: utf-8 -*- ####################################################
from django import forms
from django.utils.translation import ugettext_lazy as _

from haystack.forms import SearchForm

class HaystackSearchForm(SearchForm):
    q = forms.CharField(label=_('Keyword'), required=False)