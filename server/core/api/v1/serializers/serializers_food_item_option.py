from rest_framework import serializers

from core.models import FoodItemOption, FoodItem


class FoodItemOptionListCreateSerializer(serializers.ModelSerializer):

    foodItem = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=FoodItem.objects.all()
    )

    class Meta:
        model = FoodItemOption
        fields = [
          "id",
          "title",
          "description",
          "price",
          "foodItem",
        ]


class FoodItemOptionRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    foodItem = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=FoodItem.objects.all()
    )

    class Meta:
        model = FoodItemOption
        fields = [
          "id",
          "title",
          "description",
          "price",
          "foodItem",
        ]
