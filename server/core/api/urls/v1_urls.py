from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.api.v1.views.store_views import (
   ImageListCreateView,
   ImageRetrieveView,
   VirtualShopCreateView,
   VirtualShopRetrieveUpdateView,
   VirtualShopListFoodItemCategoryView,
   VirtualShopRetrieveUpdateAddressView,
   FoodItemCategoryCreateListView,
   FoodItemCategoryRetrieveUpdateView,
   VirtualShopCategoryCreateView,
   VirtualShopCategoryRetrieveUpdateView,
   FoodItemListCreateView,
   FoodItemRetrieveUpdateView,
   FoodItemOptionListCreateView,
   FoodItemOptionRetrieveUpdateView,
   OpeningHourCreateView,
   WeekdaysListView,
   WeekdaysListOpeningHourView, 
   TagFoodItemListCreateView, 
   IngredientItemListCreateView, 
   IngredientItemRetrieveUpdateDelete,
   FoodItemDeleteIngredientView, 
   VirtualShopListIngredientItemView,
   VirtualShopSearchListView
)

from core.api.v1.views.purchase_view import (
   OrderItemListCreateView,
   OrderItemRetrieveUpdateView,
   CartListCreateView,
   CartRetrieveUpdateView,
   OrderListCreateView,
   OrderRetrieveUpdateView,
   CartFinalizeView,
) 

from core.api.v1.views.regions_view import (
   DeliveryAddressListCreateView,
   DeliveryAddressRetrieveUpdateView
)

app_name = "v1"


schema_view = get_schema_view(
   openapi.Info(
      title="Uplit API",
      default_version='v1',
      description="A web API to be consumed for uplit app client",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="george@uplit.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path("account/", include("core.api.v1.urls.account_urls", namespace='account')),
   path("stores/", include("core.api.v1.urls.store_urls", namespace='stores')),

   # VirtualShopCategory
   path(
      "virtual-shop-categories/",
      VirtualShopCategoryCreateView.as_view(),
      name="create_category"
   ),

   path(
      "virtual-shop-categories/<int:pk>",
      VirtualShopCategoryRetrieveUpdateView.as_view(),
      name="retrieve_update_category"
   ),

   # Image
   path(
      "images/",
      ImageListCreateView.as_view(),
      name="create_list_image"
   ),

   path(
      "images/<int:pk>/",
      ImageRetrieveView.as_view(),
      name="retrieve_destroy_image"
   ),

   # Virtual Shop
   path(
      "virtual-shops/",
      VirtualShopCreateView.as_view(),
      name="create_virtualshop"
   ),

   path(
      "virtual-shops/<int:pk>/",
      VirtualShopRetrieveUpdateView.as_view(),
      name="retrieve_update_virtualshop"
   ),

   path(
      "virtual-shops/<int:pk>/food-items-categories/",
      VirtualShopListFoodItemCategoryView.as_view(),
      name="list_category_virtualshop"
   ),

   path(
      "virtual-shops/<int:pk>/address/",
      VirtualShopRetrieveUpdateAddressView.as_view(),
      name="update_virtualshop_address"
   ),
   path(
         "virtual-shops/<int:pk>/ingredients/",
         VirtualShopListIngredientItemView.as_view(),
         name="list_ingredients_from_virtualshop"
      ),
   
   path(
         "virtual-shops/search/",
         VirtualShopSearchListView.as_view(),
         name="list_search_result_for_virtualshop"
      ),

   # Food Item category
   path(
      "food-items-categories/",
      FoodItemCategoryCreateListView.as_view(),
      name="create_fooditemcategory"
   ),

   path(
      "food-items-categories/<int:pk>/",
      FoodItemCategoryRetrieveUpdateView.as_view(),
      name="retrieve_update_fooditemcategory"
   ),

   # Food Item
   path(
      "food-items/",
      FoodItemListCreateView.as_view(),
      name="create_fooditem"
   ),

   path(
      "food-items/<int:pk>/",
      FoodItemRetrieveUpdateView.as_view(),
      name="retrieve_update_fooditem"
   ),

   path(
      "food-items/<int:pk>/ingredients/",
      FoodItemDeleteIngredientView.as_view(),
      name="delete_ingredient_from_fooditem"
   ),

   # Tag Food Item
   path("tags-food-items/", TagFoodItemListCreateView.as_view(), name="list_create_tag_food_item"),

   # Ingredient Item
   path("ingredient-items/", IngredientItemListCreateView.as_view(), name="list_create_ingredient_item"),
   path("ingredient-items/<int:pk>/", IngredientItemRetrieveUpdateDelete.as_view(), name="retrieve_update_delete_ingredient_item"),

   # Food Item Options
   path(
      "food-items-options/",
      FoodItemOptionListCreateView.as_view(),
      name="create_fooditemoption"
   ),

   path(
      "food-items-options/<int:pk>/",
      FoodItemOptionRetrieveUpdateView.as_view(),
      
      name="retrieve_update_fooditemoption"
   ),

   #Order Item
   path(
      "order-items/",
      OrderItemListCreateView.as_view(),
      name="create_orderitem"
   ),

   path(
      "order-items/<int:pk>/",
      OrderItemRetrieveUpdateView.as_view(),
      name="retrieve_update_orderitem"
   ),

   #Cart
   path(
      "carts/",
      CartListCreateView.as_view(),
      name="create_cart"
   ),

   path(
      "carts/<int:pk>/",
      CartRetrieveUpdateView.as_view(),
      name="retrieve_update_cart"
   ),
   path(
         "carts/<int:pk>/finalize",
         CartFinalizeView.as_view(),
         name="finalize_cart"
      ),

   #Delivery address
   path(
      "delivery-addresses/",
      DeliveryAddressListCreateView.as_view(),
      name="create_deliveryaddress"
   ),

   path(
      "delivery-addresses/<int:pk>/",
      DeliveryAddressRetrieveUpdateView.as_view(),
      name="retrieve_update_deliveryaddress"
   ),

   #Order
   path(
      "orders/",
      OrderListCreateView.as_view(),
      name="create_order"
   ),

   path(
      "orders/<int:pk>/",
      OrderRetrieveUpdateView.as_view(),
      name="retrieve_update_order"
   ),

   #OpeningHour
   path(
      "opening-hours/",
      OpeningHourCreateView.as_view(),
      name="create_opening_hour"
   ),
   # path(
   #    "opening-hours/<int:virtualshop_id>/<slug:weekday>/",
   #    OpeningHourCreateView.as_view(),
   #    name="list_opening_hour"
   # ),

   #Weekdays
   path(
      "weekdays/",
      WeekdaysListView.as_view(),
      name="list_weekdays"
   ),
   path(
      "weekdays/<int:company_pk>/opening-hours/",
      WeekdaysListOpeningHourView.as_view(),
      name="list_weekdays"
   ),

   re_path('swagger', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]