from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet

app_name = 'vehicle'

routers = DefaultRouter()
routers.register('Vehicle', VehicleViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
