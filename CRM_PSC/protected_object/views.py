from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ClientSerializer,
    PerformerSerializer,
    PostSerializer,
    Protected_objectSerializer,
)
from .models import (
    Client,
    Performer,
    Post,
    Protected_object,
)


class ClientListView(APIView):
    def get(self, request: Request) -> Response:
        data = Client.objects.all()
        serialized = ClientSerializer(data, many=True)
        return Response({'clients': serialized.data})


class PerformerListView(APIView):
    def get(self, request: Request) -> Response:
        data = Performer.objects.all()
        serialized = PerformerSerializer(data, many=True)
        return Response({'performers': serialized.data})


class PostListView(APIView):
    def get(self, request: Request) -> Response:
        data = Post.objects.all()
        serialized = PostSerializer(data, many=True)
        return Response({'posts': serialized.data})


class Protected_objectListView(APIView):
    def get(self, request: Request) -> Response:
        data = Protected_object.objects.all()
        serialized = Protected_objectSerializer(data, many=True)
        return Response({'protected_objects': serialized.data})

