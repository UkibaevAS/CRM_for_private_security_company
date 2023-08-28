from rest_framework import serializers

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
    webcams = serializers.CharField(source='webcams.name')
    class Meta:
        model = Protected_object
        fields = "__all__"
