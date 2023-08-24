from datetime import datetime, timedelta

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from django.db.models import Q




from .serializers import (
    PassportSerializer,
    Driving_licenseSerializer,
    Security_licenseSerializer,
    Medical_certificateSerializer,
    Periodic_inspectionSerializer,
    Electrical_certificateSerializer,
    Vehicle_passportSerializer,
    Registration_certificateSerializer,
    Insurance_policySerializer,
    BriefingSerializer
)
from .models import (
    Passport,
    Driving_license,
    Security_license,
    Medical_certificate,
    Periodic_inspection,
    Electrical_certificate,
    Vehicle_passport,
    Registration_certificate,
    Insurance_policy,
    Briefing
)
timedelta1 = 30 # Количество суток до окончания срока действия документа
current_date_plus_30_day = datetime.now() + timedelta(timedelta1)  # вычисляем текущую дату + x суток


class PassportListView(APIView):
    def get(self, request: Request) -> Response:
        data = Passport.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = PassportSerializer(data, many=True)
        return Response({'document': serialized.data})


class Driving_licenseListView(APIView):
    def get(self, request: Request) -> Response:
        data = Driving_license.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = Driving_licenseSerializer(data, many=True)
        return Response({'document': serialized.data})



class Security_licenseListView(APIView):
    def get(self, request: Request) -> Response:
        data = Security_license.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = Security_licenseSerializer(data, many=True)
        return Response({'document': serialized.data})


class Medical_certificateListView(APIView):
    def get(self, request: Request) -> Response:
        data = Medical_certificate.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = Medical_certificateSerializer(data, many=True)
        return Response({'document': serialized.data})




class Periodic_inspectionListView(APIView):
    def get(self, request: Request) -> Response:
        data = Periodic_inspection.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = Periodic_inspectionSerializer(data, many=True)
        return Response({'document': serialized.data})




class Electrical_certificateListView(APIView):
    def get(self, request: Request) -> Response:
        data = Electrical_certificate.objects.filter(test_date__lte=current_date_plus_30_day)
        serialized = Electrical_certificateSerializer(data, many=True)
        return Response({'document': serialized.data})


class Vehicle_passportListView(APIView):
    def get(self, request: Request) -> Response:
        data = Vehicle_passport.objects.all()
        serialized = Vehicle_passportSerializer(data, many=True)
        return Response({'document': serialized.data})


class Registration_certificateListView(APIView):
    def get(self, request: Request) -> Response:
        data = Registration_certificate.objects.all()
        serialized = Registration_certificateSerializer(data, many=True)
        return Response({'document': serialized.data})


class Insurance_policyListView(APIView):
    def get(self, request: Request) -> Response:
        data = Insurance_policy.objects.filter(date_expiration__lte=current_date_plus_30_day)
        serialized = Insurance_policySerializer(data, many=True)
        return Response({'document': serialized.data})



class BriefingListView(APIView):
    def get(self, request: Request) -> Response:
        data = Briefing.objects.filter(data_briefing_next__lte=current_date_plus_30_day)
        serialized = BriefingSerializer(data, many=True)
        return Response({'document': serialized.data})
