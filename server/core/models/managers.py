from django.db import models
from types import Tuple

class VirtualshopManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset()
    def closest_virtualshop(user_location: Tuple):
        return super().get_queryset()