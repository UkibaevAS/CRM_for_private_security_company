from rest_framework import serializers

from .models import (
    Gun,
    Handcuffs,
    Rubber_stick,
    Special_spray,
    Armor,
    Video_recorder,
    Radio_station,
)




class GunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gun
        fields = "__all__"


class HandcuffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handcuffs
        fields = "__all__"


class Rubber_stickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubber_stick
        fields = "__all__"


class Special_spraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Special_spray
        fields = "__all__"


class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = "__all__"


class Video_recorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_recorder
        fields = "__all__"


class Radio_stationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio_station
        fields = "__all__"


