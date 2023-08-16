from rest_framework import serializers, renderers

from .models import Worker



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
        renderers = [renderers.JSONRenderer]
