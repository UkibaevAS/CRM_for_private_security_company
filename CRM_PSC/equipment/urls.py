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

routers1 = DefaultRouter()
routers1.register('gun', GunViewSet)

routers2 = DefaultRouter()
routers2.register('cuffs', HandcuffsViewSet)

routers3 = DefaultRouter()
routers3.register('_stick', Rubber_stickViewSet)

routers4 = DefaultRouter()
routers4.register('_spray', Special_sprayViewSet)

routers5 = DefaultRouter()
routers5.register('mor', ArmorViewSet)

routers6 = DefaultRouter()
routers6.register('_recorder', Video_recorderViewSet)

routers7 = DefaultRouter()
routers7.register('_station', Radio_stationViewSet)

urlpatterns = [
    path('', include(routers1.urls)),
    path('hand', include(routers2.urls)),
    path('rubber', include(routers3.urls)),
    path('special', include(routers4.urls)),
    path('ar', include(routers5.urls)),
    path('video', include(routers6.urls)),
    path('radio', include(routers7.urls)),
]
