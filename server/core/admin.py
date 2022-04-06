from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.auth import get_user_model
from .models import (
    Admin,
    Customer,
    Seller,
    Address,
    VirtualShop,
    VirtualShopCategory,
    FoodItem,
    TagFoodItem,
    OpeningHour,
    Image,
    Weekdays,
    FoodItemCategory,
    PaymentMethod,
    FoodItemOption,
    Cart,
    OrderItem,
    Order,
    DeliveryAddress, IngredientItem
)

User = get_user_model()


# models_account
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Admin)

# models_regions
admin.site.register(DeliveryAddress)
@admin.register(Address)
class AddressAdmin(OSMGeoAdmin):
    list_display = ('AddressLine1', 'AddressLine2', "location")

# models_store
admin.site.register(VirtualShop)
admin.site.register(VirtualShopCategory)
admin.site.register(FoodItem)
admin.site.register(TagFoodItem)
admin.site.register(IngredientItem)
admin.site.register(FoodItemCategory)
admin.site.register(OpeningHour)
admin.site.register(Weekdays)
admin.site.register(FoodItemOption)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# # models_purchase
admin.site.register(PaymentMethod)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
