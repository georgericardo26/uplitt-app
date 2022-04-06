from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from .models_regions import Address


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=50, blank=True, null=True)
    activate = models.BooleanField(null=False, default=False)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)
    isDeleted = models.BooleanField(null=False, default=False)

    def __repr__(self):
        return f"<User: {self.username}>"

    def __str__(self):
        return self.username

    @property
    def profile(self):
        if self.is_superuser:
            return "admin"

        profiles = ["seller", "customer"]
        for profile in profiles:
            if hasattr(self, profile):
                return profile

        return None


class Seller(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
    )

    class Meta:
        unique_together = ["user"]

    def __repr__(self):
        return f"<Seller: {self.user.username}>"

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="Male")
    birthday = models.DateTimeField(auto_now_add=True, auto_created=True)
    phoneNumber = models.CharField(max_length=50, blank=True, null=True)
    facebookId = models.CharField(max_length=15, blank=False, null=False)
    googleId = models.CharField(max_length=15, blank=False, null=False)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
    )

    address = models.ForeignKey(
        Address, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __repr__(self):
        return f"<Customer: {self.user}>"

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)




