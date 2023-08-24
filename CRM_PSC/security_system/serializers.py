from rest_framework import serializers

from .models import (
    Security_system,
    Alarm_system,
    Webcam,
)


class Security_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_system
        fields = [
            'name',
            'description',
            'owner',
            'installation_date',
            'service_date',
            'service_date_next',
        ]


class Alarm_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm_system
        fields = [
            'name',
            'description',
            'owner',
            'installation_date',
            'service_date',
            'service_date_next',
        ]


class WebcamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webcam
        fields = [
            'name',
            'description',
            'owner',
            'installation_date',
            'service_date',
            'service_date_next',
        ]
