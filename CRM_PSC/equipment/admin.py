from django.contrib import admin

from .models import Uniform, Gun, Armor, Video_recorder, Handcuffs, Rubber_stick, Special_spray, Radio_station


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


@admin.register(Handcuffs)
class HandcuffsAdmin(admin.ModelAdmin):
    list_display = "name", "description"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "factory_number"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "date_manufacture", "receipt_date", "certificate",),
        }),
    ]


@admin.register(Rubber_stick)
class Rubber_stickAdmin(admin.ModelAdmin):
    list_display = "name", "description"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name",
    fieldsets = [
        (None, {
            "fields": ("name", "description", "date_manufacture", "receipt_date", "certificate",),
        }),
    ]


@admin.register(Special_spray)
class Special_sprayAdmin(admin.ModelAdmin):
    list_display = "name", "description"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "expiration_date",
    fieldsets = [
        (None, {
            "fields": ("name", "description", "date_manufacture", "receipt_date", "certificate", "expiration_date",),
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


@admin.register(Video_recorder)
class Video_recorderAdmin(admin.ModelAdmin):
    list_display = "name", "description", "factory_number"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "factory_number"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "certificate",
                       "date_manufacture", "receipt_date", "installation_date", "maintenance_interval",
                       "service_date", "service_date_next", "maintenance_report"
                       ),
        }),
    ]


@admin.register(Radio_station)
class Radio_stationAdmin(admin.ModelAdmin):
    list_display = "name", "description", "factory_number"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "factory_number"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "factory_number", "certificate",
                       "date_manufacture", "receipt_date", "installation_date", "maintenance_interval",
                       "service_date", "service_date_next", "maintenance_report"
                       ),
        }),
    ]
