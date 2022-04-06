from django.db import models
from django.contrib.gis.db.models import PointField


class Address(models.Model):
    AddressLine1 = models.CharField(max_length=60, blank=True, null=True)
    AddressLine2 = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    postalCode = models.CharField(max_length=20, null=True, blank=True)
    stateProvinceRegion = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    city = models.CharField(max_length=50, null=True, blank=True)
    location = PointField(null=True)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<Address: {self.AddressLine1}>"

    def __str__(self):
        return self.AddressLine1 if self.AddressLine1 else None


class DeliveryAddress(Address):
    def __repr__(self):
        return f"<DeliveryAddress: {self.AddressLine1}>"
