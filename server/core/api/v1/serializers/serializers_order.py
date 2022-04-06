from rest_framework import serializers

from core.models import (
    Order,
    Cart,
)


class OrderListCreateSerializer(serializers.ModelSerializer):

    cart = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Cart.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "uuid",
            "status",
            "cart",
            "createAt",
            "updateAt"
        ]


class OrderRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    cart = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Cart.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "uuid",
            "status",
            "cart",
            "createAt",
            "updateAt"
        ]