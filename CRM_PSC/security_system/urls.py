from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    Security_systemViewSet,
    Alarm_systemViewSet,
    WebcamViewSet,
)
app_name = 'security_system'

routers1 = DefaultRouter()
routers1.register('security_system', Security_systemViewSet)

routers2 = DefaultRouter()
routers2.register('_system', Alarm_systemViewSet)

routers3 = DefaultRouter()
routers3.register('cam', WebcamViewSet)

urlpatterns = [
    path('', include(routers1.urls)),
    path('alarm', include(routers2.urls)),
    path('web', include(routers3.urls)),
]
