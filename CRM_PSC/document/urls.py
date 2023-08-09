from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    PassportViewSet,
    Driving_licenseViewSet,
    Security_licenseViewSet,
    Medical_certificateViewSet,
    Periodic_inspectionViewSet,
    Electrical_certificateViewSet,
    Vehicle_passportViewSet,
    Registration_certificateViewSet,
    Insurance_policyViewSet,
    BriefingViewSet
)

app_name = "document"

routers = DefaultRouter()
routers.register('passport', PassportViewSet)
routers.register('driving_license', Driving_licenseViewSet)
routers.register('security_license', Security_licenseViewSet)
routers.register('medical_certificate', Medical_certificateViewSet)
routers.register('periodic_inspection', Periodic_inspectionViewSet)
routers.register('electrical_certificate', Electrical_certificateViewSet)
routers.register('vehicle_passport', Vehicle_passportViewSet)
routers.register('registration_certificate', Registration_certificateViewSet)
routers.register('insurance_policy', Insurance_policyViewSet)
routers.register('briefing', BriefingViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
