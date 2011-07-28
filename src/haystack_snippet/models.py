### -*- coding: utf-8 -*- ####################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

class SearchLogger(models.Model):
    """
    Stores search queries statistic.

        - **text** -- search query text
        - **counter** -- count of this search query usage
        - **last_time** -- last time query using

    >>> obj, create = SearchLogger.objects.get_or_create(text="Some search text")
    >>> obj
    <SearchLogger: SearchLogger object>

    """
    text = models.TextField(_("Search query"))
    counter = models.IntegerField(_("Search query count"), default=1)
    last_time = models.DateTimeField(_("Search query last used"), auto_now=True)

    class Meta:
        ordering = ('-counter',)
        verbose_name = _("Search query")
        verbose_name_plural = _("Search queries")