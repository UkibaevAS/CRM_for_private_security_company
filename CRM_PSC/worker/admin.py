from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
import os

from django.contrib import admin
from django import forms

from .models import Worker


@admin.action(description="Archive worker")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive worker")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)





class WorkerForm(forms.ModelForm):
    file = forms.FileField(label="photo")

    class Meta:
        model = Worker
        fields = "__all__"


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    form = WorkerForm
    actions = [
        mark_archived,
        mark_unarchived,
    ]

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Worker/photo/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.photo = file_path
        instance.save()

# @admin.register(Worker)
# class WorkerAdmin(admin.ModelAdmin):
#     actions = [
#         mark_archived,
#         mark_unarchived,
#     ]
#
#     list_display = "first_name", "second_name", "middle_name", "archived"
#     list_display_links = "second_name",
#     ordering = "-second_name",
#     search_fields = "second_name", "archived"
#     fieldsets = [
#         (None, {
#             "fields": ("first_name", "second_name", "middle_name", "date_birth", "data_employment", "organization",
#                        "department", "position", "category", "electrical_safety_qualification", "briefings",
#                        "documents", "uniforms",
#                        ),
#         }),
#
#         ("Extra options", {
#             "fields": ("archived",),
#             "classes": ("collapse",),
#             "description": "Extra options. Field 'archived' is for soft delete",
#         }),
#         ("Images", {
#             "fields": ("foto",),
#         }),
#     ]
