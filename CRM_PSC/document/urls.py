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

routers1 = DefaultRouter()
routers1.register('passport', PassportViewSet)
routers2 = DefaultRouter()
routers2.register('_license', Driving_licenseViewSet)
routers3 = DefaultRouter()
routers3.register('_license', Security_licenseViewSet)
routers4 = DefaultRouter()
routers4.register('_certificate', Medical_certificateViewSet)
routers5 = DefaultRouter()
routers5.register('_inspection', Periodic_inspectionViewSet)
routers6 = DefaultRouter()
routers6.register('_certificate', Electrical_certificateViewSet)
routers7 = DefaultRouter()
routers7.register('_passport', Vehicle_passportViewSet)
routers8 = DefaultRouter()
routers8.register('_certificate', Registration_certificateViewSet)
routers9 = DefaultRouter()
routers9.register('_policy', Insurance_policyViewSet)
routers10 = DefaultRouter()
routers10.register('briefing', BriefingViewSet)

urlpatterns = [
    path('', include(routers1.urls)),
    path('driving', include(routers2.urls)),
    path('security', include(routers3.urls)),
    path('medical', include(routers4.urls)),
    path('periodic', include(routers5.urls)),
    path('electrical', include(routers6.urls)),
    path('vehicle', include(routers7.urls)),
    path('registration', include(routers8.urls)),
    path('insurance', include(routers9.urls)),
    path('briefing/', include(routers10.urls)),
]
