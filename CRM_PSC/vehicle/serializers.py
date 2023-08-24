from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    owner_company = serializers.CharField(source='owner_company.name')
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
    owner_company = serializers.CharField(source='owner_company.name')

    class Meta:
        model = Vehicle
        fields = [
            'name',
            'branding',
            'VIN_number',
            'license_plate',
            'owner_company',
            'owner_private',
            'date_manufacture',
            'receipt_date',
            'insurance_policy_limit',
            'mileage',
            'service_date',
            'engine_oil',
            'engine_oil_viscosity',
        ]



