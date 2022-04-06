import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.api.v1.serializers.serializers_virtualshop import VirtualShopHyperlinkedIdentitySerializer
from core.models.models_account import Customer
from core.models import Seller

logger = logging.getLogger(__name__)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "phoneNumber",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        logger.info("User created successfully!")

        return user


class SellerSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    has_virtualshop = serializers.SerializerMethodField()
    virtualshop = VirtualShopHyperlinkedIdentitySerializer(read_only=True)

    class Meta:
        model = Seller
        fields = ["pk", "user", "has_virtualshop", "virtualshop"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer(data=user_data)
        user.is_valid()
        user.save()

        seller_instance = Seller.objects.create(user=user.instance)
        return seller_instance

    def get_has_virtualshop(self, obj):
        if hasattr(obj, "virtualshop"):
            return True
        return False


class CustomerSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ["pk", "user"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer(data=user_data)
        user.is_valid()
        user.save()

        customer_instance = Customer.objects.create(user=user.instance)
        return customer_instance

