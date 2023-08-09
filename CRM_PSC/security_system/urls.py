from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    Security_systemViewSet,
    Alarm_systemViewSet,
    WebcamViewSet,
)
app_name = 'security_system'

routers = DefaultRouter()
routers.register('security_system', Security_systemViewSet)
routers.register('alarm_system', Alarm_systemViewSet)
routers.register('webcam', WebcamViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
