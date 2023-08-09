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
routers.register('client', ClientViewSet)
routers.register('performer', PerformerViewSet)
routers.register('post', PostViewSet)
routers.register('protected_object', Protected_objectViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
