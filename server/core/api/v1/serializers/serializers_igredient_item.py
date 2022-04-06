from rest_framework import serializers

from core.models import IngredientItem


class IngredientItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientItem
        fields = ["id", "name", "details", "selected", "virtualshop", "createAt", "updateAt"]


class IngredientItemToFoodItemCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(allow_blank=False, required=True)
    detail = serializers.CharField(allow_blank=False, required=False)
    selected = serializers.BooleanField(required=False)
    updateAt = serializers.CharField(allow_blank=True, required=False)
    createAt = serializers.CharField(allow_blank=True, required=False)
