from django.contrib import admin

from .models import Uniform, Gun, Armor


@admin.register(Uniform)
class UniformAdmin(admin.ModelAdmin):
    list_display = "name", "description", "size"
    list_display_links = ("name",)
    ordering = "-name", "size"
    search_fields = "name", "description", "size"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "size",),
        }),
    ]


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
