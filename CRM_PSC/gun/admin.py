from django.contrib import admin

from .models import Gun


@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    list_display = "name", "description", "factory_number"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "factory_number"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "date_test_shoot",
                       "date_manufacture", "receipt_date", "certificate",
                       ),
        }),
    ]
