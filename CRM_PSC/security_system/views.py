from rest_framework.viewsets import ModelViewSet

from .serializers import (
    Security_systemSerializer,
    Alarm_systemSerializer,
    WebcamSerializer,
)
from .models import (
    Security_system,
    Alarm_system,
    Webcam,
)


class Security_systemViewSet(ModelViewSet):
    queryset = Security_system.objects.all()
    serializer_class = Security_systemSerializer


class Alarm_systemViewSet(ModelViewSet):
    queryset = Alarm_system.objects.all()
    serializer_class = Alarm_systemSerializer


class WebcamViewSet(ModelViewSet):
    queryset = Webcam.objects.all()
    serializer_class = WebcamSerializer
