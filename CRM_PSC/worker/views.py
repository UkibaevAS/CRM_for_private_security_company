from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import WorkerSerializer, WorkerDetailSerializer
from .models import Worker


class WorkerListView(APIView):
    def get(self, request: Request) -> Response:
        data = Worker.objects.all()
        serialized = WorkerSerializer(data, many=True)
        return Response({'workers': serialized.data})
        # return Response(serialized.data)


class WorkerDetailView(APIView):
    def get(self, request, last_name):
        workers = Worker.objects.filter(second_name=last_name)
        if workers:
            serialized = WorkerDetailSerializer(workers, many=True, context={'request': request})
            return Response({'workers': serialized.data})
        else:
            return Response({"message": "Работники с указанной фамилией не найдены"}, status=404)


