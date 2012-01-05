### -*- coding: utf-8 -*- ####################################################

from haystack.query import RelatedSearchQuerySet as RelatedSearchQuerySetOld

class RelatedSearchQuerySet(RelatedSearchQuerySetOld):
    
    def __init__(self, site=None, query=None):
        super(RelatedSearchQuerySet, self).__init__(site=site, query=query)
        self._count = None
    
    def _get_count(self):
        """Returns the total number of matching results."""
        results = self.query.get_results()
        print "results --> ", results
        # Remember the search position for each result so we don't have to resort later.
        models_pks = {}
        for result in results:
            models_pks.setdefault(result.model, []).append(result.pk)
        
        total = 0
        for model in models_pks:
            for model in models_pks:
                if model in self._load_all_querysets:
                    # Use the overriding queryset.
                    total += self._load_all_querysets[model].filter(pk__in=models_pks[model]).count()
                else:
                    # Check the SearchIndex for the model for an override.
                    try:
                        qs = self.site.get_index(model).load_all_queryset()
                        total += qs.filter(pk__in=models_pks[model]).count()
                    except NotRegistered:
                        # The model returned doesn't seem to be registered with
                        # the current site. We should silently fail and populate
                        # nothing for those objects.
                        pass
        
        return total
    
    
    def count(self):
        #if self._count is None:
        #    self._count = self._get_count()

        #return self._count
        return self._get_count()
