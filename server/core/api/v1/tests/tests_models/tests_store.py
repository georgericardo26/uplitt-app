# import os
# import unittest
# from django.test import TestCase
# from django.db import DataError, IntegrityError

# from core.models.models_account import User, Seller
# from core.models.models_regions import Address
# from core.models.models_store import (
#     VirtualShop,
#     FoodItemCategory,
#     FoodItem,
#     # VirtualShopCategory,
# )


# ENV = os.getenv("SETTINGS_ENV")


# class VirtualShopModelTest(TestCase):
#     def setUp(self):
#         self.user_model = {"username": "test", "password": "abcde2021"}
#         self.address_model = {
#             "AddressLine1": "LongBeach",
#             "AddressLine2": "teste",
#             "country": "The united states",
#             "postalCode": "5151351",
#             "stateProvinceRegion": "Florida",
#             "city": "Fort Lauderdale",
#             "lat": 20.0,
#             "long": 25.0,
#         }

#         self.virtual_shop_model = {
#             "name": "Virtual_Store", "phoneNumber": "99999999"}

#     def test_relationship_seller_address_virtualShop_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)

#         virtual_shop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )

#         self.assertEqual(virtual_shop.name, self.virtual_shop_model["name"])

#         self.assertEqual(
#             virtual_shop.seller.user.username,
#             self.user_model["username"]
#         )

#         self.assertEqual(
#             virtual_shop.address.AddressLine1,
#             self.address_model["AddressLine1"]
#         )

#     def test_update_virtualShop_successful(self):
#         new_name_virtualShop = "Virtua_Store2 "

#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtual_shop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )

#         try:
#             virtual_shop.name = new_name_virtualShop
#             virtual_shop.save()

#         except Exception:
#             raise ("Something worng when trying update Virtual Shop")

#     def test_delete_virtualShop_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtual_shop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         virtual_shop.delete()

#         virtual_shop = VirtualShop.objects.filter(id=1).exists()
#         self.assertFalse(virtual_shop)


# class FoodItemCategoryModelTest(TestCase):
#     def setUp(self):
#         self.user_model = {"username": "test", "password": "abcde2021"}
#         self.address_model = {
#             "AddressLine1": "LongBeach",
#             "AddressLine2": "teste",
#             "country": "The united states",
#             "postalCode": "5151351",
#             "stateProvinceRegion": "Florida",
#             "city": "Fort Lauderdale",
#             "lat": 20.0,
#             "long": 25.0,
#         }

#         self.virtual_shop_model = {
#             "name": "Virtual_Store_name", "phoneNumber": "99999999"}

#         self.food_item_category_model = {
#             "name": "category_name",
#             "description": "category_description",
#         }

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_relationship_foodItemCategory_menu_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )

#         menu = Menu.objects.create(virtualShop=virtualShop)

#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model,
#             menu=menu
#         )

#         self.assertEqual(
#             foodItemCategory.name,
#             self.food_item_category_model['name']
#         )

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_update_foodItemCategory_successful(self):
#         new_foodItemCategory_name = "category_name_2"

#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         menu = Menu.objects.create(virtualShop=virtualShop)

#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model,
#             menu=menu
#         )

#         try:
#             foodItemCategory.name = new_foodItemCategory_name
#             menu.save()

#         except Exception:
#             raise ("Something worng when trying update Food Item Category")

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_delete_foodItemCategory_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         menu = Menu.objects.create(virtualShop=virtualShop)
#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model,
#             menu=menu
#         )

#         foodItemCategory.delete()
#         foodItemCategory = FoodItemCategory.objects.filter(id=1).exists()
#         self.assertFalse(foodItemCategory)


# class FoodItemModelTest(TestCase):
#     def setUp(self):
#         self.user_model = {"username": "test", "password": "abcde2021"}
#         self.address_model = {
#             "AddressLine1": "LongBeach",
#             "AddressLine2": "teste",
#             "country": "The united states",
#             "postalCode": "5151351",
#             "stateProvinceRegion": "Florida",
#             "city": "Fort Lauderdale",
#             "lat": 20.0,
#             "long": 25.0,
#         }

#         self.virtual_shop_model = {
#             "name": "Virtual_Store", "phoneNumber": "99999999"}

#         self.food_item_category_model = {
#             "name": "category_name",
#             "description": "category_description",
#         }

#         self.food_item = {
#             "title": "title_foodItem",
#             "description": "description_foodItem",
#         }

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_relationship_foodItem_foodItemcategory_menu_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         menu = Menu.objects.create(virtualShop=virtualShop)
#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model, menu=menu
#         )

#         foodItem = FoodItem.objects.create(
#             **self.food_item, foodItemCategory=foodItemCategory, menu=menu
#         )

#         self.assertEqual(
#             foodItem.foodItemCategory.name,
#             self.food_item_category_model["name"]
#         )

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_update_foodItem_successful(self):
#         new_fooditem_title = "title_foodItem_2"

#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         menu = Menu.objects.create(virtualShop=virtualShop)
#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model, menu=menu
#         )

#         foodItem = FoodItem.objects.create(
#             **self.food_item, foodItemCategory=foodItemCategory, menu=menu
#         )

#         try:

#             foodItem.title = new_fooditem_title
#             foodItem.save()

#         except Exception:
#             raise ("Something worng when trying update Food Item")

#     @unittest.skipIf(ENV == "uplitt_server.settings.int",
#                      "not supported in this enviroment")
#     def test_delete_foodItem_successful(self):
#         user = User.objects.create(**self.user_model)
#         seller = Seller.objects.create(user=user)
#         address = Address.objects.create(**self.address_model)
#         virtualShop = VirtualShop.objects.create(
#             **self.virtual_shop_model,
#             address=address,
#             seller=seller,
#         )
#         menu = Menu.objects.create(virtualShop=virtualShop)
#         foodItemCategory = FoodItemCategory.objects.create(
#             **self.food_item_category_model, menu=menu
#         )

#         foodItem = FoodItem.objects.create(
#             **self.food_item, foodItemCategory=foodItemCategory, menu=menu
#         )

#         foodItem.delete()
#         foodItem = FoodItem.objects.filter(id=1).exists()
#         self.assertFalse(foodItem)
