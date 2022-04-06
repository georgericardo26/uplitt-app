import os
import unittest

from django.test import TestCase
from django.db import DataError, IntegrityError
from core.models.models_regions import Address

ENV = os.getenv("SETTINGS_ENV")


class AddressModelTest(TestCase):
    def setUp(self):
        self.address_model = {"AddressLine1": "879, Wall Street"}

    def test_create_address_successful(self):
        address = Address.objects.create(**self.address_model)
        self.assertEqual(address.AddressLine1, self.address_model["AddressLine1"])

    def test_update_address_successful(self):
        new_AddressLine1 = "123, Green Street"
        address = Address.objects.create(**self.address_model)

        try:
            address.AddressLine1 = new_AddressLine1
            address.save()

        except Exception:
            raise ("Something worng when trying update address")

    def test_delete_address_successful(self):
        address = Address.objects.create(**self.address_model)
        address.delete()

        address = Address.objects.filter(id=1).exists()
        self.assertFalse(address)

    @unittest.skipIf(ENV == "uplitt_server.settings.int",
                     "not supported in this enviroment")
    def test_create_address_invalid(self):

        with self.assertRaises(DataError):
            Address.objects.create(
                AddressLine1=(
                    "address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_"
                    "address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address"
                )
            )

    @unittest.skipIf(ENV == "uplitt_server.settings.int",
                     "not supported in this enviroment")
    def test_update_address_invalid(self):
        address = Address.objects.create(**self.address_model)
        with self.assertRaises(DataError):
            address.AddressLine1 = (
                "address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_"
                "address_address_address_address_address_address_address_address_address_address_address_address_address_address_address_address"
            )
            address.save()
