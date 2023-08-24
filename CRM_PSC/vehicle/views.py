from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import VehicleSerializer, VehicleDetailSerializer
from .models import Vehicle


class VehicleistView(APIView):
    def get(self, request: Request) -> Response:
        data = Vehicle.objects.all()
        serialized = VehicleSerializer(data, many=True)
        return Response({'vehicle': serialized.data})


class VehicleDetailView(APIView):
    def get(self, request, license_plate):
        vehicle = Vehicle.objects.filter(license_plate=f'{license_plate}RUS')
        if vehicle:
            serialized = VehicleDetailSerializer(vehicle, many=True, context={'request': request})
            return Response({'vehicle': serialized.data})
        else:
            return Response({"message": "Автомобиль не найден"}, status=404)

