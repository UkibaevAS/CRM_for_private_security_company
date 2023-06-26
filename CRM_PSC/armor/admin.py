from django.contrib import admin

from .models import Armor


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = "name", "description", "factory_number", "protection_category"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "protection_category"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "protection_category",
                       "date_manufacture", "date_purchase", "certificate",
                       ),
        }),
    ]
