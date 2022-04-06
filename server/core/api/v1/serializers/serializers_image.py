from rest_framework import serializers

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["id", "upload", "name", "url"]
        extra_kwargs = {'upload': {'write_only': True},
                        'name': {'write_only': True}}

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.upload.url)
