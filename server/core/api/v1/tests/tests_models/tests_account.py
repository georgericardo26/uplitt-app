import os
import unittest

from django.contrib.auth import get_user_model
from django.db import DataError, IntegrityError
from django.test import TestCase
from core.models.models_account import Seller, Customer
from core.models.models_regions import Address

User = get_user_model()
ENV = os.getenv("SETTINGS_ENV")


class UserModelTest(TestCase):
    def setUp(self):
        self.user_model = {"username": "test", "password": "abcde2021"}

    def test_create_user_successful(self):
        user = User.objects.create(**self.user_model)
        user.set_password(self.user_model["password"])

        self.assertEqual(user.username, self.user_model["username"])
        self.assertTrue(user.check_password(self.user_model["password"]))

    def test_update_user_successful(self):
        new_username = "test2"
        user = User.objects.create(**self.user_model)

        try:
            user.username = new_username
            user.save()

        except Exception:
            raise ("Something worng when trying update user")

    def test_delete_user_successful(self):
        user = User.objects.create(**self.user_model)
        user.delete()

        user = User.objects.filter(id=1).exists()
        self.assertFalse(user)

    @unittest.skipIf(ENV == "uplitt_server.settings.int",
                     "not supported in this enviroment")
    def test_create_invalid_user(self):
        with self.assertRaises(DataError):
            User.objects.create(
                username="username_long_username_long_username_long_username_long_username_long_username_long_username_long_username_long_username_long_username_long_username_long_username_long"
            )

    @unittest.skipIf(ENV == "uplitt_server.settings.int",
                     "not supported in this enviroment")
    def test_update_user_invalid(self):
        User.objects.create(**self.user_model)
        with self.assertRaises(IntegrityError):
            User.objects.create(username="test")


class SellerModelTest(TestCase):
    def setUp(self):
        self.user_model = {"username": "test", "password": "abcde2021"}

    def test_relationship_seller_successful(self):
        user = User.objects.create(**self.user_model)
        seller = Seller.objects.create(user=user)
        self.assertEqual(seller.user.username, self.user_model["username"])


class CustomerModelTest(TestCase):
    def setUp(self):
        self.user_model = {"username": "test", "password": "abcde2021"}
        self.address_model = {"AddressLine1":"LongBeach",
                            "AddressLine2": "teste",
                            "country": "The united states",
                            "postalCode": "5151351",
                            "stateProvinceRegion":"Florida",
                            "city":"Fort Lauderdale",
                            "lat": 20.0,
                            "long":25.0,}

    def test_relationship_user_customer_successful(self):
        user = User.objects.create(**self.user_model)
        customer = Customer.objects.create(user=user)
        self.assertEqual(customer.user.username, self.user_model["username"])

    def test_relationship_address_customer_successful(self):
        user = User.objects.create(**self.user_model)
        address = Address.objects.create(**self.address_model)
        customer = Customer.objects.create(address=address,user=user)
        self.assertEqual(customer.address.AddressLine1, self.address_model["AddressLine1"])
        self.assertEqual(customer.address.AddressLine2, self.address_model["AddressLine2"])        
        self.assertEqual(customer.address.country, self.address_model["country"])
        self.assertEqual(customer.address.postalCode, self.address_model["postalCode"])
        self.assertEqual(customer.address.stateProvinceRegion, self.address_model["stateProvinceRegion"])
        self.assertEqual(customer.address.city, self.address_model["city"])
        self.assertEqual(customer.address.lat, self.address_model["lat"])
        self.assertEqual(customer.address.long, self.address_model["long"])                                                
