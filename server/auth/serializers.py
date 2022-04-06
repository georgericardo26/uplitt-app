from django.conf import settings
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    expires_in = serializers.IntegerField()
    token_type = serializers.CharField()
    scope = serializers.CharField()
    refresh_token = serializers.CharField()
