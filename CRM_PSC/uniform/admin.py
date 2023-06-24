from django.contrib import admin

from .models import Uniform


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
