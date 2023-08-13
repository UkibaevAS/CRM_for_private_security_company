from datetime import datetime, timedelta

from rest_framework.viewsets import ModelViewSet
# from django.db.models import Q


timedelta1 = 60

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


class PassportViewSet(ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer


class Driving_licenseViewSet(ModelViewSet):


    current_date_plus_x = datetime.now() + timedelta(timedelta1)  # вычисляем текущую дату + x суток
    queryset = Driving_license.objects.filter(date_expiration__lte=current_date_plus_x)
    serializer_class = Driving_licenseSerializer


class Security_licenseViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Security_license.objects.filter(date_expiration__lte=current_date_plus_x)
    serializer_class = Security_licenseSerializer


class Medical_certificateViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Medical_certificate.objects.filter(date_expiration__lte=current_date_plus_x)
    serializer_class = Medical_certificateSerializer


class Periodic_inspectionViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Periodic_inspection.objects.filter(date_expiration__lte=current_date_plus_x)
    serializer_class = Periodic_inspectionSerializer


class Electrical_certificateViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Electrical_certificate.objects.filter(test_date__lte=current_date_plus_x)
    serializer_class = Electrical_certificateSerializer


class Vehicle_passportViewSet(ModelViewSet):
    queryset = Vehicle_passport.objects.all()
    serializer_class = Vehicle_passportSerializer


class Registration_certificateViewSet(ModelViewSet):
    queryset = Registration_certificate.objects.all()
    serializer_class = Registration_certificateSerializer


class Insurance_policyViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Insurance_policy.objects.filter(date_expiration__lte=current_date_plus_x)
    serializer_class = Insurance_policySerializer


class BriefingViewSet(ModelViewSet):
    current_date_plus_x = datetime.now() + timedelta(timedelta1)
    queryset = Briefing.objects.filter(data_briefing_next__lte=current_date_plus_x)
    serializer_class = BriefingSerializer
