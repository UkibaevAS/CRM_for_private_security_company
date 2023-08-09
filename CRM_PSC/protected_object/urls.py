from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ClientViewSet,
    PerformerViewSet,
    PostViewSet,
    Protected_objectViewSet,
)

app_name = 'protected_object'

routers = DefaultRouter()
routers.register('Client', ClientViewSet)
routers.register('Performer', PerformerViewSet)
routers.register('Post', PostViewSet)
routers.register('Protected_object', Protected_objectViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
