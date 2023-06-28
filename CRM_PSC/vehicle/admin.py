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
            "fields": ("name", "branding", "VIN_number", "license_plate",
                       "date_manufacture", "date_purchase", "registration_certificate_number",
                       "reg_certificate_number_copy", "passport_number", "passport_copy", "number_insurance_policy",
                       "date_expiration_insurance", "is_listed_insurance", "mileage", "service_date", "engine_oil",
                       "engine_oil_viscosity", "radio_stations", "video_recorders", "armors",
                       ),
        }),
    ]
