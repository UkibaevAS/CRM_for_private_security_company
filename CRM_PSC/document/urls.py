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
routers.register('Passport', PassportViewSet)
routers.register('Driving_license', Driving_licenseViewSet)
routers.register('Security_license', Security_licenseViewSet)
routers.register('Medical_certificate', Medical_certificateViewSet)
routers.register('Periodic_inspection', Periodic_inspectionViewSet)
routers.register('Electrical_certificate', Electrical_certificateViewSet)
routers.register('Vehicle_passport', Vehicle_passportViewSet)
routers.register('Registration_certificate', Registration_certificateViewSet)
routers.register('Insurance_policy', Insurance_policyViewSet)
routers.register('Briefing', BriefingViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]
