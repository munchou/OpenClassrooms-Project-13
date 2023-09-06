from django.test import TestCase
from django.urls import reverse


class OCLettingsSiteViewsTest(TestCase):
    def test_lettings_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Letting Test")

    # def test_lettings_letting(self):
    #     response = self.client.get(reverse("lettings:letting", args=[1]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "lettings/letting.html")
    #     self.assertContains(response, "Letting Test")

    # def test_letting_error500(self):
    #     response = self.client.get(reverse("lettings:letting", args=[456452312]))
    #     self.assertTemplateUsed(response, "500.html")
