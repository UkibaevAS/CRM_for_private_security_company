from django.contrib import admin
from django import forms

from .models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = "__all__"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm