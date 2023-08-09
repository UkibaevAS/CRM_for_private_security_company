from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.views import hello_view, NumberEmployeesViewSet

routers = DefaultRouter()
routers.register('workers', NumberEmployeesViewSet)

app_name = "api"

urlpatterns = [
    path('hello/', hello_view, name='Hi'),
    #path('number_employees/', NumberEmployees.as_view(), name='NumberEmployees'),
    path('worker', include(routers.urls)),
]