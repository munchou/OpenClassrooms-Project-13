from django.test import TestCase
from django.urls import reverse

from ..models import Address, Letting


class LettingsViewsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=42,
            street="Rue du Couperet",
            city="Pompouy-Saint-Poulet",
            state="BG",
            zip_code=21340,
            country_iso_code="FR",
        )
        self.letting = Letting.objects.create(
            title="Letting Test", address=self.address
        )

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "Letting Test")