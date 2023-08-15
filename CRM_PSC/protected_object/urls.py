from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ClientViewSet,
    PerformerViewSet,
    PostViewSet,
    Protected_objectViewSet,
)

app_name = 'protected_object'

routers1 = DefaultRouter()
routers1.register('client', ClientViewSet)

routers2 = DefaultRouter()
routers2.register('former', PerformerViewSet)

routers3 = DefaultRouter()
routers3.register('st', PostViewSet)

routers4 = DefaultRouter()
routers4.register('_object', Protected_objectViewSet)

urlpatterns = [
    path('', include(routers1.urls)),
    path('per', include(routers2.urls)),
    path('po', include(routers3.urls)),
    path('protected', include(routers4.urls)),
]
