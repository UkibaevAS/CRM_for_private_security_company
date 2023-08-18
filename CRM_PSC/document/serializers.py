from rest_framework import serializers

from .models import (
    Passport,
    Driving_license,
    Security_license,
    Medical_certificate,
    Periodic_inspection,
    Electrical_certificate,
    Vehicle_passport,
    Registration_certificate,
    Insurance_policy,
    Briefing
)


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = [
            'owner',
            'date_expiration',
        ]


class Driving_licenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving_license
        fields = [
            'owner',
            'date_expiration',
        ]


class Security_licenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_license
        fields = [
            'owner',
            'date_expiration',
        ]


class Medical_certificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_certificate
        fields = [
            'owner',
            'date_expiration',
        ]


class Periodic_inspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodic_inspection
        fields = [
            'owner',
            'date_expiration',
        ]


class Electrical_certificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electrical_certificate
        fields = [
            'owner',
            'date_expiration',
        ]


class Vehicle_passportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_passport
        fields = "__all__"


class Registration_certificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration_certificate
        fields = "__all__"


class Insurance_policySerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance_policy
        fields = [
            'owner',
            'date_expiration',
        ]


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = [
            'owner',
            'data_briefing_next',
        ]
