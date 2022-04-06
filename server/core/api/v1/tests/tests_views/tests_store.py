import json
import unittest

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

from auth.tests.utils import GetTokenTest
from core.models.models_account import Seller
from core.models.models_regions import Address
from core.models.models_store import VirtualShop, FoodItemCategory, FoodItem

User = get_user_model()


class VirtualShopViewTest(APITestCase):

    url_create_virtualshop = "api:v1:stores:create_virtualshop"
    url_retrieve_update_virtualshop = "api:v1:stores:retrieve_update_virtualshop"

    SELLER = {"user": {"username": "user1", "password": "user1"}}

    VIRTUALSHOP = {
        "name": "Store_Fake",
        "phoneNumber": "00000000",
        "address": {
            "AddressLine1": "Street A, Light Zonehf",
            "AddressLine2": "Offfice number 4f5",
            "city": "Logs Angeles",
            "stateProvinceRegion": "Californifa",
            "country": "USAe",
            "postalCode": "0000e0000",
        },
    }

    def setUp(self):
        user = User.objects.create_user(**self.SELLER["user"])
        self.seller = Seller.objects.create(user=user)
        self.token_client = GetTokenTest()

        self.token_data = self.token_client.get_token(
            self.SELLER["user"]["username"], self.SELLER["user"]["password"]
        )

        token_dict = json.loads(self.token_data.content)
        token = token_dict["access_token"]
        self.header = {"Authorization": f"Bearer {token}"}

    @unittest.skip("Todo: Update test")
    def test_create_vistualShop_successful(self):

        response = self.client.post(
            reverse(
                self.url_create_virtualshop,
            ),
            data=self.VIRTUALSHOP,
            **self.header,
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        response_dict = json.loads(response.content)

        self.assertEqual(response_dict["name"], self.VIRTUALSHOP["name"])
        self.assertEqual(
            response_dict["address"]["AddressLine1"],
            self.VIRTUALSHOP["address"]["AddressLine1"],
        )

    @unittest.skip("Todo: Update test")
    def test_retrieve_vistualShop_successful(self):

        response_post = self.client.post(
            reverse(
                self.url_create_virtualshop,
            ),
            data=self.VIRTUALSHOP,
            **self.header,
        )

        virtualShop_post = json.loads(response_post.content)
        kwargs = virtualShop_post["pk"]

        response_get = self.client.get(
            reverse(
                self.url_retrieve_update_virtualshop,
                kwargs={"pk": kwargs},
            ),
            **self.header,
        )

        self.assertEqual(status.HTTP_200_OK, response_get.status_code)

        virtualShop_get = json.loads(response_get.content)

        self.assertEqual(virtualShop_get["name"], self.VIRTUALSHOP["name"])
        self.assertEqual(
            virtualShop_get["address"]["AddressLine1"],
            self.VIRTUALSHOP["address"]["AddressLine1"],
        )
        
class FoodItemCategoryViewTest(APITestCase):

    url_create_fooditemcategory = "api:v1:stores:create_fooditemcategory"
    url_retrieve_update_fooditemcategory = (
        "api:v1:stores:retrieve_update_fooditemcategory"
    )

    SELLER = {"user": {"username": "user1", "password": "user1"}}

    ADDRESS = {
        "AddressLine1": "Street A, Light Zonehf",
        "AddressLine2": "Offfice number 4f5",
        "city": "Logs Angeles",
        "stateProvinceRegion": "Californifa",
        "country": "USAe",
        "postalCode": "0000e0000",
    }

    VIRTUALSHOP = {
        "name": "Store_Fake",
        "phoneNumber": "00000000",
    }

    FOODITEMCATEGORY = {"name": "name_test", "description": "description_test"}

    def setUp(self):
        user = User.objects.create_user(**self.SELLER["user"])
        self.seller = Seller.objects.create(user=user)
        self.token_client = GetTokenTest()

        self.token_data = self.token_client.get_token(
            self.SELLER["user"]["username"], self.SELLER["user"]["password"]
        )

        token_dict = json.loads(self.token_data.content)
        token = token_dict["access_token"]
        self.header = {"Authorization": f"Bearer {token}"}

        address = Address.objects.create(**self.ADDRESS)

        virtualShop = VirtualShop.objects.create(
            **self.VIRTUALSHOP,
            seller=self.seller,
            address=address,
        )

        menu = Menu.objects.create(virtualShop=virtualShop)

        self.foodItemCategory = {
            "name": self.FOODITEMCATEGORY["name"],
            "description": self.FOODITEMCATEGORY["description"],
            "menu": menu.id,
        }

    @unittest.skip("Todo: Update test")
    def test_create_foodItemCategory_successful(self):

        response = self.client.post(
            reverse(
                self.url_create_fooditemcategory,
            ),
            data=self.foodItemCategory,
            **self.header,
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        response_dict = json.loads(response.content)

        self.assertEqual(response_dict["name"], self.foodItemCategory["name"])
        
    @unittest.skip("Todo: Update test")
    def test_retrieve_foodItemCategory_successful(self):

        response_post = self.client.post(
            reverse(
                self.url_create_fooditemcategory,
            ),
            data=self.foodItemCategory,
            **self.header,
        )

        foodItemCategory_post = json.loads(response_post.content)
        kwargs = foodItemCategory_post["id"]

        response_get = self.client.get(
            reverse(
                self.url_retrieve_update_fooditemcategory,
                kwargs={"pk": kwargs},
            ),
            **self.header,
        )

        self.assertEqual(status.HTTP_200_OK, response_get.status_code)

        foodItemCategory_get = json.loads(response_get.content)

        self.assertEqual(foodItemCategory_get["name"], self.foodItemCategory["name"])


class FoodItemViewTest(APITestCase):

    url_create_fooditem = "api:v1:stores:create_fooditem"
    url_retrieve_update_fooditem = "api:v1:stores:retrieve_update_fooditem"

    SELLER = {"user": {"username": "user1", "password": "user1"}}

    ADDRESS = {
        "AddressLine1": "Street A, Light Zonehf",
        "AddressLine2": "Offfice number 4f5",
        "city": "Logs Angeles",
        "stateProvinceRegion": "Californifa",
        "country": "USAe",
        "postalCode": "0000e0000",
    }

    VIRTUALSHOP = {
        "name": "Store_Fake",
        "phoneNumber": "00000000",
    }

    MENU = {
        "name": "menu_test",
        "description": "description_tes",
    }

    FOODITEMCATEGORY = {"name": "name_test", "description": "description_test"}

    FOODITEM = {"title": "title_foodItem", "description": "description_foodItem"}

    def setUp(self):
        user = User.objects.create_user(**self.SELLER["user"])
        self.seller = Seller.objects.create(user=user)
        self.token_client = GetTokenTest()

        self.token_data = self.token_client.get_token(
            self.SELLER["user"]["username"], self.SELLER["user"]["password"]
        )

        token_dict = json.loads(self.token_data.content)
        token = token_dict["access_token"]
        self.header = {"Authorization": f"Bearer {token}"}

        address = Address.objects.create(**self.ADDRESS)

        virtualShop = VirtualShop.objects.create(
            **self.VIRTUALSHOP,
            seller=self.seller,
            address=address,
        )

        menu = Menu.objects.create(**self.MENU, virtualShop=virtualShop)

        foodItemCategory = FoodItemCategory.objects.create(
            **self.FOODITEMCATEGORY, menu=menu
        )

        self.foodItem = {
            "title": self.FOODITEM["title"],
            "description": self.FOODITEM["description"],
            "menu": menu.id,
            "foodItemCategory": foodItemCategory.id,
        }

    @unittest.skip("Todo: Update test")
    def test_create_foodItem_successful(self):

        response = self.client.post(
            reverse(
                self.url_create_fooditem,
            ),
            data=self.foodItem,
            **self.header,
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        response_dict = json.loads(response.content)

        self.assertEqual(response_dict["title"], self.foodItem["title"])

    @unittest.skip("Todo: Update test")
    def test_retrieve_foodItem_successful(self):

        response_post = self.client.post(
            reverse(
                self.url_create_fooditem,
            ),
            data=self.foodItem,
            **self.header,
        )

        foodItem_post = json.loads(response_post.content)
        kwargs = foodItem_post["id"]

        response_get = self.client.get(
            reverse(
                self.url_retrieve_update_fooditem,
                kwargs={"pk": kwargs},
            ),
            **self.header,
        )

        self.assertEqual(status.HTTP_200_OK, response_get.status_code)

        foodItem_get = json.loads(response_get.content)

        self.assertEqual(foodItem_get["title"], self.foodItem["title"])
