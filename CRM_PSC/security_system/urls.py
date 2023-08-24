from django.urls import path

from .views import (
    Security_systemListView,
    Alarm_systemListView,
    WebcamListView,
)
app_name = 'security_system'


urlpatterns = [
    path('', Security_systemListView.as_view(), name='security_system'),
    path('alarm_system', Alarm_systemListView.as_view(), name='alarm_system'),
    path('webcam', WebcamListView.as_view(), name='webcam'),
]
