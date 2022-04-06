from rest_framework import serializers

from core.api.v1.serializers.serializers_order_item import OrderItemListCreateSerializer
from core.models import (
    Cart,
    Customer,
    DeliveryAddress
)


class CartListCreateSerializer(serializers.ModelSerializer):

    customer = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Customer.objects.all()
    )

    deliveryAddress = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=DeliveryAddress.objects.all()
    )

    class Meta:
        model = Cart
        fields = [
            "id",
            "uuid",
            "customer",
            "deliveryAddress",
            "orderItem",
            "activate",
            "createAt",
            "updateAt",
            "orderItem"
        ]
        extra_kwargs = {
            "activate": {"read_only": True},
            "deliveryAddress": {"read_only": True},
            "orderItem": {"read_only": True}
        }


class CartRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    customer = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Customer.objects.all()
    )

    deliveryAddress = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=DeliveryAddress.objects.all()
    )

    class Meta:
        model = Cart
        fields = [
            "id",
            "uuid",
            "customer",
            "deliveryAddress",
            "activate",
            "createAt",
            "updateAt",
        ]
