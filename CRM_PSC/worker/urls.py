from django.urls import path
from .views import WorkerListView, WorkerDetailView


app_name = "worker"


urlpatterns = [
    path('', WorkerListView.as_view(), name='workers'),
    path('info/', WorkerDetailView.as_view(), name='workers_info'),
]

