from rest_framework import generics, permissions
from rest_framework.response import Response

from core.api.v1.serializers.serializers_order_item import (
    OrderItemListCreateSerializer,
    OrderItemRetrieveUpdateDestroySerializer,
)
from core.api.v1.serializers.serializers_cart import (
    CartListCreateSerializer,
    CartRetrieveUpdateDestroySerializer,
)
from core.api.v1.serializers.serializers_order import (
    OrderListCreateSerializer,
    OrderRetrieveUpdateDestroySerializer,
)

from core.models import (
    Order,
    OrderItem,
    Cart, DeliveryAddress, FoodItem
)


class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class OrderItemRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    

class CartRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class CartFinalizeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def update(self, request, *args, **kwargs):
        cart = Cart.objects.get(pk=kwargs["pk"])
        cart.activate = False
        cart.save()

        order = Order.objects.create(cart=cart)
        serializer = OrderListCreateSerializer(instance=order, context={"request": self.request})

        return Response(data=serializer.data, status=200)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    

class OrderRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

