import os

from django.contrib import admin
from django import forms

from .models import Affiliated_company, Department, Position


class Affiliated_companyForm(forms.ModelForm):
    # file = forms.FileField(label="contract")

    class Meta:
        model = Affiliated_company
        fields = "__all__"


@admin.register(Affiliated_company)
class Affiliated_companyAdmin(admin.ModelAdmin):
    form = Affiliated_companyForm


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
