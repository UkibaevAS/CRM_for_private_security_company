from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .serializers import WorkerSerializer
from .models import Worker


# class WorkerViewSet(ModelViewSet):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
#     filter_backends = [
#         SearchFilter,
#     ]
#     search_fields = ['second_name']
class WorkerViewSet(APIView):
    def get(self, request: Request) -> Response:
        workers = Worker.objects.all()
        serialized = WorkerSerializer(workers, many=True)
        return Response({'workers': serialized})

class WorkerWithCategoryViewSet(ModelViewSet):
    queryset = Worker.objects.exclude(category='Нет разряда')
    serializer_class = WorkerSerializer

    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})

class WorkerWithoutCategoryViewSet(ModelViewSet):
    queryset = Worker.objects.filter(category='Нет разряда')
    serializer_class = WorkerSerializer
