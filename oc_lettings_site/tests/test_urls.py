from django.test import TestCase
from django.urls import reverse, resolve

from ..views import index


class OCLettingsSiteURLsTest(TestCase):
    def test_oclettingssite_url_index(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)
