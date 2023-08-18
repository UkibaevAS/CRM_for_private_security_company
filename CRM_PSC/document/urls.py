from django.urls import path, include


from .views import (
    PassportListView,
    Driving_licenseListView,
    Security_licenseListView,
    Medical_certificateListView,
    Periodic_inspectionListView,
    Electrical_certificateListView,
    Vehicle_passportListView,
    Registration_certificateListView,
    Insurance_policyListView,
    BriefingListView,
)

app_name = "document"




urlpatterns = [
    path('passport/', PassportListView.as_view(), name='passport'),
    path('driving_license/', Driving_licenseListView.as_view(), name='driving_license'),
    path('security_license/', Security_licenseListView.as_view(), name='security_license'),
    path('medical_certificate/', Medical_certificateListView.as_view(), name='medical_certificate'),
    path('periodic_inspection/', Periodic_inspectionListView.as_view(), name='periodic_inspection'),
    path('electrical_certificate/', Electrical_certificateListView.as_view(), name='electrical_certificate'),
    path('vehicle_passport', Vehicle_passportListView.as_view(), name='vehicle_passport'),
    path('registration_certificate', Registration_certificateListView.as_view(), name='registration_certificate'),
    path('insurance_policy', Insurance_policyListView.as_view(), name='insurance_policy'),
    path('briefing/', BriefingListView.as_view(), name='briefing'),
]
