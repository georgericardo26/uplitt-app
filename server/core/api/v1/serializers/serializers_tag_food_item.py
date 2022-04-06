from rest_framework import serializers

from core.models import TagFoodItem


class TagFoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagFoodItem
        fields = "__all__"
