### -*- coding: utf-8 -*- ####################################################

import random

from .models import SearchLogger
from .forms import ExtendedSearchForm

MIN_FONT_SIZE = 12
MAX_FONT_SIZE = 24


def search_sidebar(request):
    words = list(SearchLogger.objects.all().order_by('-counter')[:10])
    random.shuffle(words)
    if words:
        counters = [ word.counter for word in words ]
        mx = max(counters)
        mn = min(counters)
        step = float(mx - mn) / float(MAX_FONT_SIZE - MIN_FONT_SIZE) or (MAX_FONT_SIZE - MIN_FONT_SIZE) / 2
        words = [{'text': word.text,
                  'size': MIN_FONT_SIZE + int((word.counter - mn) / step),
                  'color': "%x" % random.randint(0, 16777215),
                 } for word in words ]
    return { 
        'search_words': words,
        'SEARCH_FORM': ExtendedSearchForm(request.GET or None, prefix='search') 
    }
