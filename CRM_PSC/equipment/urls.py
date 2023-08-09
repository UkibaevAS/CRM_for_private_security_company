from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    GunViewSet,
    HandcuffsViewSet,
    Rubber_stickViewSet,
    Special_sprayViewSet,
    ArmorViewSet,
    Video_recorderViewSet,
    Radio_stationViewSet,
)

app_name = 'equipment'

routers = DefaultRouter()
routers.register('Gun', GunViewSet)
routers.register('Handcuffs', HandcuffsViewSet)
routers.register('Rubber_stick', Rubber_stickViewSet)
routers.register('Special_spray', Special_sprayViewSet)
routers.register('Armor', ArmorViewSet)
routers.register('Video_recorder', Video_recorderViewSet)
routers.register('Radio_station', Radio_stationViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
