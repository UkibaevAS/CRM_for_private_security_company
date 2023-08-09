from rest_framework.viewsets import ModelViewSet

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


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class PerformerViewSet(ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Protected_objectViewSet(ModelViewSet):
    queryset = Protected_object.objects.all()
    serializer_class = Protected_objectSerializer

