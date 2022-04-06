import logging

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.api.v1.serializers.serializers_food_item import FoodItemSerializer, FoodItemBaseSerializer, \
    FoodItemIngredientListSerializer
from core.api.v1.serializers.serializers_image import ImageSerializer
from core.api.v1.serializers.serializers_regions import AddressSerializer
from core.api.v1.serializers.serializers_virtual_shop_category import VirtualShopCategorylinkedIdentitySerializer, VirtualShopCategorySerializer
from core.models import VirtualShop, FoodItemCategory, Seller, Image, IngredientItem

logger = logging.getLogger(__name__)


class VirtualShopHyperlinkedIdentitySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:v1:retrieve_update_virtualshop",
        read_only=True,
        lookup_field="pk"
    )

    class Meta:
        model = VirtualShop
        fields = ["id", "url", "name"]


class VirtualShopListFoodItemCategorySerializer(serializers.ModelSerializer):
    foodItems = FoodItemBaseSerializer(many=True, read_only=True)

    class Meta:
        model = FoodItemCategory
        fields = ["id", "title", "description", "foodItems"]


class VirtualShopSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    seller = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Seller.objects.all()
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="api:v1:retrieve_update_virtualshop",
        read_only=True,
        lookup_field="pk"
    )

    class Meta:
        model = VirtualShop
        fields = ["id", "name", "phoneNumber", "seller", "address", "virtualShopCategory", "image", "url"]

    def create(self, validated_data):
        logger.info("Preparing to create a virtual store.")

        # Get seller
        seller_id = validated_data.pop("seller")
        seller = get_object_or_404(Seller, pk=seller_id)
        validated_data["seller"] = seller

        # Save address
        address_data = validated_data.pop("address")
        address = AddressSerializer().create(address_data)

        validated_data["address"] = address

        # Create Virtual Shop
        instance = VirtualShop.objects.create(**validated_data)

        logger.info("Virtual Store was created successfully!")
        return instance

    def get_virtualshop_image(self, obj):
        serializer = ImageSerializer(instance=obj.image, context=self.context)
        return serializer.data


class VirtualShopUpdateSerializer(serializers.ModelSerializer):

    address = AddressSerializer(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Seller.objects.all()
    )

    class Meta:
        model = VirtualShop
        fields = "__all__"


class VirtualShopListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualShop
        fields = ["id", "name", "phoneNumber", "seller", "address", "image_pk", "image"]


class VirtualShopListIngredientItemSerializer(serializers.ModelSerializer):

    foodItems = FoodItemIngredientListSerializer(many=True)

    class Meta:
        model = IngredientItem
        fields = "__all__"


class VirtualShopSearchListSerializer(VirtualShopSerializer):
    seller = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Seller.objects.all()
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="api:v1:retrieve_update_virtualshop",
        read_only=True,
        lookup_field="pk"
    )
    virtualShopCategory = VirtualShopCategorySerializer(many=True)
    foodItems = serializers.SerializerMethodField()

    class Meta:
        model = VirtualShop
        fields = ["id", "name", "seller", "virtualShopCategory", "foodItems", "image", "url"]

    def create(self, validated_data):
        return super(VirtualShopSearchListSerializer, self).create(validated_data)
    
    def get_foodItems(self, obj):
        items = obj.foodItems.all()[:10]
        serializer = FoodItemBaseSerializer(data=items, many=True, context=self.context)
        serializer.is_valid()

        return serializer.data
