import os

from django.contrib import admin
from django import forms

from .models import Security_system, Alarm_system, Webcam


class Security_systemForm(forms.ModelForm):

    class Meta:
        model = Security_system
        fields = "__all__"
@admin.register(Security_system)
class GunAdmin(admin.ModelAdmin):
    form = Security_systemForm
    ordering = ['license_plate']
@admin.register(Security_system)
class GunAdmin(admin.ModelAdmin):
    form = Security_systemForm
    ordering = ['license_plate']

@admin.register(Security_system)
class GunAdmin(admin.ModelAdmin):
    form = Security_systemForm
    ordering = ['license_plate']


class Alarm_systemForm(forms.ModelForm):

    class Meta:
        model = Alarm_system
        fields = "__all__"


@admin.register(Alarm_system)
class Alarm_systemAdmin(admin.ModelAdmin):
    form = Alarm_systemForm


class WebcamForm(forms.ModelForm):

    class Meta:
        model = Webcam
        fields = "__all__"


@admin.register(Webcam)
class WebcamAdmin(admin.ModelAdmin):
    form = WebcamForm
