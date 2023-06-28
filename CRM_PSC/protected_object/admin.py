from django.contrib import admin

from .models import Post, Protected_object, Client


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "name", "phone"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "phone"
    fieldsets = [
        (None, {
            "fields": (
                "name", "protection_mode", "start_day_shift", "start_day_shift_free_day", "start_night_shift", "phone",
                "number_per_day", "number_per_night", "armors", "guns", "radio_stations", "webcams", "alarm_systems",
                "vehicles",
            ),
        }),
    ]


@admin.register(Protected_object)
class Protected_objectAdmin(admin.ModelAdmin):
    list_display = "name", "address", "curator",
    list_display_links = "name", "address", "curator",
    ordering = "-name", "address", "curator",
    search_fields = "name", "address" "phone"
    fieldsets = [
        (None, {
            "fields": (
                "name", "address", "curator", "security_method", "posts", "foto", "security_systems", "clients",
            ),
        }),
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = "name", "phone", "address",
    list_display_links = "name",
    ordering = "-name", "address",
    search_fields = "name", "address"
    fieldsets = [
        (None, {
            "fields": ("name", "address", "phone", "email", "INN", "OGRN", "bank_details", "director", "contact_person",
                       "phone_contact_person", "security_contracts",
                       ),
        }),
    ]
