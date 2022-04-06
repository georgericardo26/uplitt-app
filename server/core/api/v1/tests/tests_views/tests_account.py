import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from auth.tests.utils import GetTokenTest


from django.contrib.auth import get_user_model
from core.models.models_account import Seller

User = get_user_model()


class SellerViewTest(APITestCase):

    url_create_seller = "api:v1:account:create_seller"
    url_retrieve_update_destroy_seller = "api:v1:account:retrieve_update_destroy_seller"

    SELLER = {"user": {"username": "user1", "password": "user1"}}

    def setUp(self):
        user = User.objects.create_user(**self.SELLER["user"])
        self.seller = Seller.objects.create(user=user)
        self.token_client = GetTokenTest()

    def get_token(self, username, password):
        return self.token_client.get_token(username, password)

    def test_create_seller_successful(self):
        self.SELLER["user"]["username"] = "user2"
        response = self.client.post(reverse(self.url_create_seller), data=self.SELLER)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn("pk", response.data)
        self.assertIn("user", response.data)

        self.assertIn("username", response.data["user"])

    def test_retrieve_seller_successful(self):
        token_data = self.get_token(
            self.SELLER["user"]["username"], self.SELLER["user"]["password"]
        )

        token_dict = json.loads(token_data.content)
        token = token_dict["access_token"]
        header = {"Authorization": f"Bearer {token}"}

        response = self.client.get(
            reverse(
                self.url_retrieve_update_destroy_seller,
                kwargs={"pk": self.seller.pk},
            ),
            **header,
        )
        response_dict = json.loads(response.content)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(
            response_dict["user"]["username"], self.SELLER["user"]["username"]
        )

    def test_delete_seller_successful(self):

        token_data = self.get_token(
            self.SELLER["user"]["username"], self.SELLER["user"]["password"]
        )

        token_dict = json.loads(token_data.content)
        token = token_dict["access_token"]
        header = {"Authorization": f"Bearer {token}"}

        response = self.client.delete(
            reverse(
                self.url_retrieve_update_destroy_seller,
                kwargs={"pk": self.seller.user_id},
            ),
            **header,
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        seller_id = self.seller.user_id
        seller_delete = Seller.objects.filter(user_id=seller_id).exists()
        self.assertFalse(seller_delete)
