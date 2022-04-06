from rest_framework import serializers

from core.api.v1.serializers.serializers_opening_hour import OpeningHourSerializer
from core.models import Weekdays


class WeekdaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weekdays
        fields = [
            "id",
            "name",
            "createAt",
            "updateAt"
        ]

class WeekdaysListOpeningHourSerializer(serializers.ModelSerializer):

    opening_hours = OpeningHourSerializer(many=True)

    class Meta:
        model = Weekdays
        fields = [
            "id",
            "name",
            "opening_hours"
        ]