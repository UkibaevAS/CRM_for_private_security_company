from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import WorkerViewSet


app_name = "worker"

routers = DefaultRouter()
routers.register('workers', WorkerViewSet)



urlpatterns = [
    path('api/', include(routers.urls)),
]