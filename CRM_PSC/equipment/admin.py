import os

from django.contrib import admin
from django import forms

from .models import Uniform, Gun, Armor, Video_recorder, Handcuffs, Rubber_stick, Special_spray, Radio_station


@admin.register(Uniform)
class UniformAdmin(admin.ModelAdmin):
    list_display = "name", "description", "size"
    list_display_links = ("name",)
    ordering = "-name", "size"
    search_fields = "name", "description", "size"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "size", "owner",),
        }),
    ]


class GunForm(forms.ModelForm):

    class Meta:
        model = Gun
        fields = "__all__"


@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    form = GunForm



class HandcuffsForm(forms.ModelForm):

    class Meta:
        model = Handcuffs
        fields = "__all__"


@admin.register(Handcuffs)
class HandcuffsAdmin(admin.ModelAdmin):
    form = HandcuffsForm



class Rubber_stickForm(forms.ModelForm):

    class Meta:
        model = Rubber_stick
        fields = "__all__"


@admin.register(Rubber_stick)
class Rubber_stickAdmin(admin.ModelAdmin):
    form = Rubber_stickForm



class Special_sprayForm(forms.ModelForm):

    class Meta:
        model = Special_spray
        fields = "__all__"


@admin.register(Special_spray)
class Special_sprayAdmin(admin.ModelAdmin):
    form = Special_sprayForm



class ArmorForm(forms.ModelForm):

    class Meta:
        model = Armor
        fields = "__all__"


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    form = ArmorForm


class Video_recorderForm(forms.ModelForm):
    class Meta:
        model = Video_recorder
        fields = "__all__"


@admin.register(Video_recorder)
class Video_recorderAdmin(admin.ModelAdmin):
    form = Video_recorderForm


class Radio_stationForm(forms.ModelForm):

    class Meta:
        model = Radio_station
        fields = "__all__"


@admin.register(Radio_station)
class Radio_stationAdmin(admin.ModelAdmin):
    form = Radio_stationForm

