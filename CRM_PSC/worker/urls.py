from django.urls import path
from .views import WorkerListView


app_name = "worker"


urlpatterns = [
    path('worker_view', WorkerListView.as_view(), name='worker_view'),
]

