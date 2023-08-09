from rest_framework.viewsets import ModelViewSet

from .serializers import VehicleSerializer
from .models import Vehicle


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

