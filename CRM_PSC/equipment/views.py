from rest_framework.viewsets import ModelViewSet

from .serializers import (
    GunSerializer,
    HandcuffsSerializer,
    Rubber_stickSerializer,
    Special_spraySerializer,
    ArmorSerializer,
    Video_recorderSerializer,
    Radio_stationSerializer,
)
from .models import (
    Gun,
    Handcuffs,
    Rubber_stick,
    Special_spray,
    Armor,
    Video_recorder,
    Radio_station,
)


class GunViewSet(ModelViewSet):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer


class HandcuffsViewSet(ModelViewSet):
    queryset = Handcuffs.objects.all()
    serializer_class = HandcuffsSerializer


class Rubber_stickViewSet(ModelViewSet):
    queryset = Rubber_stick.objects.all()
    serializer_class = Rubber_stickSerializer


class Special_sprayViewSet(ModelViewSet):
    queryset = Special_spray.objects.all()
    serializer_class = Special_spraySerializer


class ArmorViewSet(ModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class Video_recorderViewSet(ModelViewSet):
    queryset = Video_recorder.objects.all()
    serializer_class = Video_recorderSerializer


class Radio_stationViewSet(ModelViewSet):
    queryset = Radio_station.objects.all()
    serializer_class = Radio_stationSerializer
