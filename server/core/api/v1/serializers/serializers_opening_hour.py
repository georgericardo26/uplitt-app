from rest_framework import serializers
from core.models import OpeningHour, VirtualShop, Weekdays


class OpeningHourSerializer(serializers.ModelSerializer):

    virtualShop = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=VirtualShop.objects.all()
    )

    weekDay = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Weekdays.objects.all()
    )

    class Meta:
        model = OpeningHour
        fields = [
            "id",
            "name",
            "virtualShop",
            "weekDay",
            "startTime",
            "endTime",
            "createAt",
            "updateAt"
        ]
