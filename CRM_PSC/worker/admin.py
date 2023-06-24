from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Worker


@admin.action(description="Archive worker")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive worker")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]

    list_display = "first_name", "second_name", "middle_name", "archived"
    list_display_links = "second_name",
    ordering = "-second_name",
    search_fields = "second_name", "archived"
    fieldsets = [
        (None, {
            "fields": ("first_name", "second_name", "middle_name", "date_birth", "data_employment",
                       "department", "position", "category", "electrical_safety_qualification", "briefings",
                       "documents", "uniforms",
                       ),
        }),

        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field 'archived' is for soft delete",
        }),
        ("Images", {
            "fields": ("foto",),
        }),
    ]
