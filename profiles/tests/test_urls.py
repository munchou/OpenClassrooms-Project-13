from django.test import TestCase
from django.urls import reverse, resolve

from ..views import index, profile


class ProfilesURLsTest(TestCase):
    def test_profiles_url_index(self):
        url = reverse("profiles:index")
        self.assertEqual(resolve(url).func, index)

    def test_profiles_url_profile(self):
        url = reverse("profiles:profile", args=["testouilleur"])
        self.assertEqual(resolve(url).func, profile)
