from rest_framework import serializers
from core.models import VirtualShopCategory


class VirtualShopCategorylinkedIdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualShopCategory
        fields = ["id", "name"]


class VirtualShopCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualShopCategory
        fields = '__all__'  # ["id", "title", "description"]


class VirtualShopCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualShopCategory
        fields = '__all__'  # ["id", "title", "description", "virtual_shop"]
