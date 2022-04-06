from .account_views import (
  SellerCreateView, 
  SellerRetrieveUpdateDestroyView,
  CustomerCreateView,
  CustomerRetrieveUpdateDestroyView,
)

from .store_views import (
  VirtualShopCreateView,
  VirtualShopRetrieveUpdateView,
  VirtualShopRetrieveUpdateAddressView,
  VirtualShopListFoodItemCategoryView,
  VirtualShopCategoryCreateView,
  VirtualShopCategoryRetrieveUpdateView,
  FoodItemCategoryCreateListView,
  FoodItemCategoryRetrieveUpdateView,
  FoodItemListCreateView,
  FoodItemRetrieveUpdateView,
  ImageListCreateView,
  ImageRetrieveView,
)