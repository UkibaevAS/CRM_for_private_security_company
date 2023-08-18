from rest_framework import serializers

from .models import Worker



class WorkerSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='organization.name')
    class Meta:
        model = Worker
        fields = [
            'official_employment',
            'organization',
            'category',
            'electrical_safety_qualification',
        ]


class WorkerDetailSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='organization.name')
    class Meta:
        model = Worker
        fields = [
            'first_name',
            'middle_name',
            'second_name',
            'photo',
            'phone',
            'address',
            'date_birth',
            'official_employment',
            'organization',
            'category',
        ]
