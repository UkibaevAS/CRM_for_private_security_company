import os

from django.contrib import admin
from django import forms

from config.models import Affiliated_company, Department, Position


class Affiliated_companyForm(forms.ModelForm):
    file = forms.FileField(label="contract")

    class Meta:
        model = Affiliated_company
        fields = "__all__"


@admin.register(Affiliated_company)
class Affiliated_companyAdmin(admin.ModelAdmin):
    form = Affiliated_companyForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Affiliated_company/contracts/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.contract = file_path
        instance.save()

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = "name", "manager",
    list_display_links = ("name",)
    ordering = "-name",
    search_fields = "name", "manager",
    fieldsets = [
        (None, {
            "fields": ("name", "manager",),
        }),
    ]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = "name",
    list_display_links = ("name",)
    ordering = "-name",
    search_fields = "name",
    fieldsets = [
        (None, {
            "fields": ("name",),
        }),
    ]
