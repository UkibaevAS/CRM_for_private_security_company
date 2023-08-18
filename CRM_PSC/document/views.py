from datetime import datetime, timedelta

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from django.db.models import Q


timedelta1 = 60 # За количество суток до окончания срока действия документа

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


class PassportListView(APIView):
    def get(self, request: Request) -> Response:
        data = Passport.objects.all()
        serialized = PassportSerializer(data, many=True)
        return Response({'passports': serialized.data})



class Driving_licenseListView(APIView):
    def get(self, request: Request) -> Response:
        data = Driving_license.objects.all()
        serialized = Driving_licenseSerializer(data, many=True)
        return Response({'driving_license': serialized.data})

    # current_date_plus_x = datetime.now() + timedelta(timedelta1)  # вычисляем текущую дату + x суток
    # queryset = Driving_license.objects.filter(date_expiration__lte=current_date_plus_x)
    # serializer_class = Driving_licenseSerializer


class Security_licenseListView(APIView):
    def get(self, request: Request) -> Response:
        data = Security_license.objects.all()
        serialized = Security_licenseSerializer(data, many=True)
        return Response({'security_license': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Security_license.objects.filter(date_expiration__lte=current_date_plus_x)
    # serializer_class = Security_licenseSerializer


class Medical_certificateListView(APIView):
    def get(self, request: Request) -> Response:
        data = Medical_certificate.objects.all()
        serialized = Medical_certificateSerializer(data, many=True)
        return Response({'medical_certificate': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Medical_certificate.objects.filter(date_expiration__lte=current_date_plus_x)
    # serializer_class = Medical_certificateSerializer


class Periodic_inspectionListView(APIView):
    def get(self, request: Request) -> Response:
        data = Periodic_inspection.objects.all()
        serialized = Periodic_inspectionSerializer(data, many=True)
        return Response({'periodic_inspection': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Periodic_inspection.objects.filter(date_expiration__lte=current_date_plus_x)
    # serializer_class = Periodic_inspectionSerializer


class Electrical_certificateListView(APIView):
    def get(self, request: Request) -> Response:
        data = Electrical_certificate.objects.all()
        serialized = Electrical_certificateSerializer(data, many=True)
        return Response({'electrical_certificate': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Electrical_certificate.objects.filter(test_date__lte=current_date_plus_x)
    # serializer_class = Electrical_certificateSerializer


class Vehicle_passportListView(APIView):
    queryset = Vehicle_passport.objects.all()
    serializer_class = Vehicle_passportSerializer


class Registration_certificateListView(APIView):
    queryset = Registration_certificate.objects.all()
    serializer_class = Registration_certificateSerializer


class Insurance_policyListView(APIView):
    def get(self, request: Request) -> Response:
        data = Insurance_policy.objects.all()
        serialized = Insurance_policySerializer(data, many=True)
        return Response({'insurance_policy': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Insurance_policy.objects.filter(date_expiration__lte=current_date_plus_x)
    # serializer_class = Insurance_policySerializer


class BriefingListView(APIView):
    def get(self, request: Request) -> Response:
        data = Briefing.objects.all()
        serialized = BriefingSerializer(data, many=True)
        return Response({'passports': serialized.data})
    # current_date_plus_x = datetime.now() + timedelta(timedelta1)
    # queryset = Briefing.objects.filter(data_briefing_next__lte=current_date_plus_x)
    # serializer_class = BriefingSerializer
