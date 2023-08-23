from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'license_plate',
            'owner_private',
            'owner_company',
            'branding',
            'mileage',
            'service_date',

        ]

class VehicleDetailSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='organization.name')
    photo = serializers.SerializerMethodField()
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'VIN_number',
            'date_manufacture',
            'receipt_date',
            'engine_oil',
            'engine_oil_viscosity',
            'license_plate',
            'owner_private',
            'owner_company',
            'branding',
        ]

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo:  # Проверяем, что фото существует
            return request.build_absolute_uri(obj.photo.url)
        return None

