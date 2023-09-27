from django.test import TestCase
from django.urls import reverse


class OCLettingsSiteViewsTest(TestCase):
    def test_lettings_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "oc_lettings_site/index.html")

    def test_page_not_found(self):
        response = self.client.get("/letting/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
