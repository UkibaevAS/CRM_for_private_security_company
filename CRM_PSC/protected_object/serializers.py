from rest_framework import serializers

from security_system.serializers import (
    WebcamSerializer,
    Security_systemSerializer,
    Alarm_systemSerializer,
)
from worker.serializers import WorkerDetailSerializer
from .models import (
    Client,
    Performer,
    Post,
    Protected_object,
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class Protected_objectSerializer(serializers.ModelSerializer):
    curator = WorkerDetailSerializer
    posts = PostSerializer(many=True)
    client = ClientSerializer
    performer = PerformerSerializer
    webcams = WebcamSerializer(many=True)
    security_systems = Security_systemSerializer(many=True)
    alarm_systems = Alarm_systemSerializer(many=True)
    class Meta:
        model = Protected_object
        fields = "__all__"
