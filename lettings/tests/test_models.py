from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Address, Letting


class AddressModelsTest(TestCase):
    def setUp(self):
        Address.objects.create(
            number=42,
            street="Rue du Couperet",
            city="Pompouy-Saint-Poulet",
            state="BG",
            zip_code=21340,
            country_iso_code="FRA",
        )

    def test_address_fields(self):
        address = Address.objects.get(id=1)
        address_num = address.number
        address_street = address.street
        address_city = address.city
        address_state = address.state
        address_zip_code = address.zip_code
        address_country_iso_code = address.country_iso_code
        self.assertEqual(address_num, 42)
        self.assertEqual(address_street, "Rue du Couperet")
        self.assertEqual(address_city, "Pompouy-Saint-Poulet")
        self.assertEqual(address_state, "BG")
        self.assertEqual(address_zip_code, 21340)
        self.assertEqual(address_country_iso_code, "FRA")

    def test_address_representation(self):
        address = Address.objects.get(id=1)
        self.assertEqual(str(address), "42 Rue du Couperet")

    def test_address_maxnum(self):
        # with self.assertRaisesMessage(ValidationError, "error in number length"):
        with self.assertRaises(ValidationError):
            Address(
                number=10000,
                street="Rue du Couperet",
                city="Pompouy-Saint-Poulet",
                state="BG",
                zip_code=21340,
                country_iso_code="FRA",
            ).full_clean()

    def test_address_maxlength(self):
        with self.assertRaises(ValidationError):
            Address(
                number=42,
                street="""Rue du Couperet après celle de Guillotin, en face du bar-tabac
                 la Coucougnette""",
                city="Pompouy-Saint-Poulet",
                state="BG",
                zip_code=21340,
                country_iso_code="FRA",
            ).full_clean()


class LettingModelsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=42,
            street="Rue du Couperet",
            city="Pompouy-Saint-Poulet",
            state="BG",
            zip_code=21340,
            country_iso_code="FRA",
        )
        self.letting = Letting.objects.create(
            title="Letting Test", address=self.address
        )

    def test_letting_representation(self):
        self.assertEqual(str(self.letting), "Letting Test")
