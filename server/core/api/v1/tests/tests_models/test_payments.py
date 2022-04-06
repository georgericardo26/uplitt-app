import os
from core.models.models_account import Customer
from core.models.models_purchase import PaymentMethod
import unittest
from django.contrib.auth import get_user_model
from django.db import DataError, IntegrityError
from django.test import TestCase

User = get_user_model()
ENV = os.getenv("SETTINGS_ENV")

class PaymentMethodsModelTest(TestCase):
    def setUp(self):
        self.user_model = {"username": "test", "password": "abcde2021"}
        self.customer = {
            "gender" : "Male",
            "facebookId": "44422444",
            "googleId":"3322233",
        }
        self.payment_method_model = {"stripeToken":"AFDJ#FHIFH!$IFHNNFQLFQNFEQ",
                            "type": "Debit",
                            "principal": "True",                    
                     }

    def test_create_payment_method_successful(self):
        user = User.objects.create(**self.user_model)
        customer = Customer.objects.create(**self.customer,user=user)
        payment_method = PaymentMethod.objects.create(**self.payment_method_model,customer=customer)
        
        self.assertEqual(payment_method.stripeToken, self.payment_method_model ["stripeToken"])
        self.assertEqual(payment_method.type, self.payment_method_model ["type"])
        self.assertEqual(payment_method.principal, self.payment_method_model ["principal"])