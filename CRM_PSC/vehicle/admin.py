from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = "name", "license_plate"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "license_plate"
    fieldsets = [
        (None, {
            "fields": ("name", "branding", "VIN_number", "license_plate", "date_manufacture", "date_purchase", "owner",
                       "registration_certificate", "passport_copy", "insurance_policy_limit", "is_listed_insurance",
                       "date_expiration_insurance", "insurance_policy_copy", "mileage", "service_date", "engine_oil",
                       "engine_oil_viscosity", "radio_stations", "video_recorders", "armors",
                       ),
        }),
    ]
