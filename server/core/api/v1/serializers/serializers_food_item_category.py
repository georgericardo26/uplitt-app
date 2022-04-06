from rest_framework import serializers

from core.models import VirtualShop, FoodItemCategory


class FoodItemCategoryHyperlinkedIdentitySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:v1:retrieve_update_fooditemcategory",
        read_only=True,
        lookup_field="pk"
    )

    class Meta:
        model = FoodItemCategory
        fields = ["id", "url", "title"]


class FoodItemCategorySerializer(serializers.ModelSerializer):
    virtualshop = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=VirtualShop.objects.all(),
        required=False
    )

    class Meta:
        model = FoodItemCategory
        fields = ["id", "title", "description", "virtualshop"]


class FoodItemCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemCategory
        fields = "__all__"
