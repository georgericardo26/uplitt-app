from rest_framework import serializers

from core.api.v1.serializers import FoodItemSerializer
from core.models import (
    OrderItem,
    FoodItem,
    FoodItemOption,
    Cart,
)


class OrderItemListCreateSerializer(serializers.ModelSerializer):

    foodItem = FoodItemSerializer(read_only=True)
    foodItem_pk = serializers.IntegerField(write_only=True, required=True)
    cart = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=False
    )

    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "quantity",
            "total",
            "foodItem",
            "foodItem_pk",
            "cart"
        ]

    def get_total(self, obj):
        return obj.total()

    def create(self, validated_data):

        request = self.context["request"]

        cart, created = Cart.objects.get_or_create(activate=True, customer__pk=request.user.customer.pk)

        foodItem = FoodItem.objects.get(pk=validated_data["foodItem_pk"])

        if not created:

            # Check if the current opened cart contain product from the same virtualshop
            current_virtualshop = cart.orderItem.last().foodItem.foodItemCategory.virtualshop.pk
            next_virtualshop = foodItem.foodItemCategory.virtualshop.pk

            if current_virtualshop != next_virtualshop:
                raise serializers.ValidationError("You need finalize the current cart or empty it.")

        else:
            # If the cart is new, save the new customer
            cart.customer = request.user.customer
            cart.save()

        orderItem = OrderItem.objects.create(quantity=validated_data["quantity"],
                                             foodItem=foodItem,
                                             cart=cart)

        return orderItem


class OrderItemRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    foodItem = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=FoodItem.objects.all()
    )

    foodItemOptions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=FoodItemOption.objects.all()
    )

    cart = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Cart.objects.all()
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "quantity",
            "total",
            "foodItem",
            "foodItemOptions",
            "cart",
        ]
