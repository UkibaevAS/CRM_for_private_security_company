from rest_framework.viewsets import ModelViewSet


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
    queryset = Driving_license.objects.all()
    serializer_class = Driving_licenseSerializer


class Security_licenseViewSet(ModelViewSet):
    queryset = Security_license.objects.all()
    serializer_class = Security_licenseSerializer


class Medical_certificateViewSet(ModelViewSet):
    queryset = Medical_certificate.objects.all()
    serializer_class = Medical_certificateSerializer


class Periodic_inspectionViewSet(ModelViewSet):
    queryset = Periodic_inspection.objects.all()
    serializer_class = Periodic_inspectionSerializer


class Electrical_certificateViewSet(ModelViewSet):
    queryset = Electrical_certificate.objects.all()
    serializer_class = Electrical_certificateSerializer


class Vehicle_passportViewSet(ModelViewSet):
    queryset = Vehicle_passport.objects.all()
    serializer_class = Vehicle_passportSerializer


class Registration_certificateViewSet(ModelViewSet):
    queryset = Registration_certificate.objects.all()
    serializer_class = Registration_certificateSerializer


class Insurance_policyViewSet(ModelViewSet):
    queryset = Insurance_policy.objects.all()
    serializer_class = Insurance_policySerializer


class BriefingViewSet(ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
