### -*- coding: utf-8 -*- ####################################################

from django.contrib import admin
from .models import SearchLogger

class SearchLoggerAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('text', 'counter', 'last_time')
    date_hierarchy = 'last_time'

admin.site.register(SearchLogger, SearchLoggerAdmin)