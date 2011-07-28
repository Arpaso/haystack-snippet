### -*- coding: utf-8 -*- ####################################################

from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase


class SearchingTestCase(TestCase):

    fixtures = ['development.json', ]

    def search_simple(self):
        c = Client()
        response = c.get("%s?search_q=%s" % (reverse('haystack_search'), 'somesearchquestion'))
        self.assertEqual(response.status_code, 200)
        # query in popular searches
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'somesearchquestion')
        


