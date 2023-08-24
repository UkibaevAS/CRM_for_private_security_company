from django.urls import path, include


from .views import VehicleistView, VehicleDetailView

app_name = 'vehicle'



urlpatterns = [
    path('', VehicleistView.as_view(), name='vehicle'),
    path('info/<str:license_plate>/', VehicleDetailView.as_view(), name='vehicle_info'),
]
