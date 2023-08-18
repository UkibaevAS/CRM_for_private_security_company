from rest_framework import serializers

from .models import Worker



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'official_employment',
            'organization',
            'category',
            'electrical_safety_qualification',
        ]
