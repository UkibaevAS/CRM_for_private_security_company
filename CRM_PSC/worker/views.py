from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .serializers import WorkerSerializer
from .models import Worker


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [
        SearchFilter,
    ]
    search_fields = ['second_name']
