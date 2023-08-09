from rest_framework import serializers

from .models import (
    Security_system,
    Alarm_system,
    Webcam,
)


class Security_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_system
        fields = "__all__"


class Alarm_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm_system
        fields = "__all__"


class WebcamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webcam
        fields = "__all__"
