from core.api.v1.serializers import AddressSerializer
from core.models import DeliveryAddress


class DeliveryAddressListCreateSerializer(AddressSerializer):

    class Meta:
        model = DeliveryAddress


class DeliveryAddressRetrieveUpdateDestroySerializer(DeliveryAddressListCreateSerializer):
    pass
