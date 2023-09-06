from django.test import TestCase
from django.urls import reverse, resolve

from ..views import index, letting


class LettingsURLsTest(TestCase):
    def test_lettings_url_index(self):
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, index)

    def test_lettings_url_letting(self):
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)
