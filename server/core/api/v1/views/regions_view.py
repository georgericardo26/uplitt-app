from rest_framework import generics, permissions

from core.api.v1.serializers.serializers_delivery_address import (
    DeliveryAddressListCreateSerializer,
    DeliveryAddressRetrieveUpdateDestroySerializer,
)

from core.models import DeliveryAddress


class DeliveryAddressListCreateView(generics.ListCreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    

class DeliveryAddressRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
