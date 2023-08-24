from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

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


class Security_systemListView(APIView):
    def get(self, request: Request) -> Response:
        data = Security_system.objects.all()
        serialized = Security_systemSerializer(data, many=True)
        return Response({'security_system': serialized.data})



class Alarm_systemListView(APIView):
    def get(self, request: Request) -> Response:
        data = Alarm_system.objects.all()
        serialized = Alarm_systemSerializer(data, many=True)
        return Response({'alarm_system': serialized.data})


class WebcamListView(APIView):
    def get(self, request: Request) -> Response:
        data = Webcam.objects.all()
        serialized = WebcamSerializer(data, many=True)
        return Response({'webcam': serialized.data})