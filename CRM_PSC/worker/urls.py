from django.urls import path
from .views import WorkerListView


app_name = "worker"


urlpatterns = [
    path('', WorkerListView.as_view(), name='workers_info'),
]

