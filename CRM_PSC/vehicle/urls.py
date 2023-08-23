from django.urls import path, include


from .views import VehicleistView, VehicleDetailView

app_name = 'vehicle'



urlpatterns = [
    path('', VehicleistView.as_view(), name='vehicle'),
    path('info/<str:last_name>/', VehicleDetailView.as_view(), name='vehicle_info'),
]
