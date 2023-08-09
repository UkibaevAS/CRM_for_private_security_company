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
routers.register('gun', GunViewSet)
routers.register('handcuffs', HandcuffsViewSet)
routers.register('rubber_stick', Rubber_stickViewSet)
routers.register('special_spray', Special_sprayViewSet)
routers.register('armor', ArmorViewSet)
routers.register('video_recorder', Video_recorderViewSet)
routers.register('radio_station', Radio_stationViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
