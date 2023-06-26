from django.contrib import admin

from .models import Alarm_system


@admin.register(Alarm_system)
class Alarm_systemAdmin(admin.ModelAdmin):
    list_display = "name", "description", "factory_number"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "description"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "certificate",
                       "date_manufacture", "receipt_date", "installation_date", "maintenance_interval",
                       "service_date", "service_date_next", "maintenance_report"
                       ),
        }),
    ]
