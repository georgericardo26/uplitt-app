import json
import unittest
from unittest import mock

from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase, RequestFactory
from django.urls import reverse

from auth.tests.utils import GetTokenTest
from auth.views import AuthView

User = get_user_model()


class UserAuthTest(TestCase):
    url_name = "create_token"

    USER = {
        "username": "testuser",
        "password": "pass2000@",
        "email": "test@test.com"
    }

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(**self.USER)
        self.token_client = GetTokenTest()

        self.data = {
            **self.token_client.data,
            "username": self.USER["username"],
            "password": self.USER["password"]
        }

    def get_authentication_object(self, username, password):
        return self.token_client.get_token(username, password)

    @unittest.skip("Todo: Update test")
    @mock.patch('auth.views.AuthView.create_token_response')
    def test_auth_user_successfully(self, mock_create_token_response):
        auth_obj = self.get_authentication_object(self.USER["username"], self.USER["password"])
        response_token = json.loads(auth_obj.content.decode("utf-8"))

        mock_create_token_response.return_value = (
            None, {}, json.dumps(response_token), 200
        )

        request = self.factory.post(reverse(self.url_name),
                                    data=self.data,
                                    content_type="application/json")
        response = AuthView.as_view()(request)

        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", decoded_response)
        self.assertIn("expires_in", decoded_response)
        self.assertIn("token_type", decoded_response)
        self.assertIn("scope", decoded_response)
        self.assertIn("refresh_token", decoded_response)

    def test_auth_oauth2_provider_response_with_invalid_username(self):
        self.USER["username"] = "aaaa"
        response = self.get_authentication_object(self.USER["username"], self.USER["password"])

        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("invalid_grant", decoded_response.values())

    def test_auth_oauth2_provider_response_with_invalid_password(self):
        self.USER["password"] = "0000"
        response = self.get_authentication_object(self.USER["username"], self.USER["password"])

        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("invalid_grant", decoded_response.values())
