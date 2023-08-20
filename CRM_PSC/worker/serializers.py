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
    photo = serializers.SerializerMethodField()
    class Meta:
        model = Worker
        fields = [
            'first_name',
            'middle_name',
            'second_name',
            'photo',
            'phone',
            'date_birth',
            'official_employment',
            'organization',
            'category',
        ]

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo:  # Проверяем, что фото существует
            return request.build_absolute_uri(obj.photo.url)
        return None
