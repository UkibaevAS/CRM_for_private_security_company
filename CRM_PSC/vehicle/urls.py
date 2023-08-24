from django.urls import path, include


from .views import VehicleListView, VehicleDetailView

app_name = 'vehicle'



urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle'),
    path('info/<str:license_plate>/', VehicleDetailView.as_view(), name='vehicle_info'),
]
