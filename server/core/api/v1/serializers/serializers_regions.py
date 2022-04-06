import logging

from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import fromstr
from rest_framework import serializers

from core.models import Address, VirtualShop

logger = logging.getLogger(__name__)


class AddressSerializer(serializers.ModelSerializer):
    latitude = serializers.CharField(required=False, allow_blank=True)
    longitude = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Address
        fields = [
            "pk",
            "AddressLine1",
            "AddressLine2",
            "city",
            "stateProvinceRegion",
            "country",
            "postalCode",
            "location",
            "latitude",
            "longitude"
        ]
        extra_kwargs = {
            "AddressLine1": {"required": True},
            "location": {"read_only": True}
        }

    def create(self, validated_data):
        validated_data = self.update_location_data(validated_data)
        instance = Address.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        validated_data = self.update_location_data(validated_data)
        instance = Address.objects.update(**validated_data)
        return instance

    def update_location_data(self, validated_data):
        location = None
        latitude = validated_data.pop("latitude")
        longitude = validated_data.pop("longitude")

        if latitude and longitude:
            location = fromstr(f'POINT({latitude} {longitude})', srid=4326)

        validated_data["location"] = location

        return validated_data


class AddressVirtualShopUpdateSerializer(AddressSerializer):

    def update(self, instance, validated_data):
        view = self.context.get("view")
        pk = view.kwargs.get("pk")

        virtualshop = get_object_or_404(VirtualShop, pk=pk)

        for key, value in validated_data.items():
            virtualshop.address.__dict__[key] = value

        virtualshop.save()

        return virtualshop.address
