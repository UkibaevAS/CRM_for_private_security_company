from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import WorkerSerializer
from .models import Worker


class WorkerListView(APIView):
    def get(self, request: Request) -> Response:
        data = Worker.objects.prefetch_related("organization")
        serialized = WorkerSerializer(data, many=True)
        return Response({'workers': serialized.data})

