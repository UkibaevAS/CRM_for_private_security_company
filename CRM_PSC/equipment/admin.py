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
    file = forms.FileField(label="Certificate")

    class Meta:
        model = Gun
        fields = "__all__"


@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    form = GunForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Equipment/gun/certificate/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.certificate = file_path
        instance.save()


class HandcuffsForm(forms.ModelForm):
    file = forms.FileField(label="Certificate")

    class Meta:
        model = Handcuffs
        fields = "__all__"


@admin.register(Handcuffs)
class HandcuffsAdmin(admin.ModelAdmin):
    form = HandcuffsForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Equipment/handcuffs/certificate/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.certificate = file_path
        instance.save()


class Rubber_stickForm(forms.ModelForm):
    file = forms.FileField(label="Certificate")

    class Meta:
        model = Rubber_stick
        fields = "__all__"


@admin.register(Rubber_stick)
class Rubber_stickAdmin(admin.ModelAdmin):
    form = Rubber_stickForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Equipment/rubber_stick/certificate/{pk}/{filename}".format(pk=instance.pk,
                                                                                extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.certificate = file_path
        instance.save()


class Special_sprayForm(forms.ModelForm):
    file = forms.FileField(label="Certificate")

    class Meta:
        model = Special_spray
        fields = "__all__"


@admin.register(Special_spray)
class Special_sprayAdmin(admin.ModelAdmin):
    form = Special_sprayForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Equipment/special_spray/certificate/{pk}/{filename}".format(pk=instance.pk,
                                                                                 extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.certificate = file_path
        instance.save()


class ArmorForm(forms.ModelForm):
    file = forms.FileField(label="Certificate")

    class Meta:
        model = Armor
        fields = "__all__"


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    form = ArmorForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Equipment/armor/certificate/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.certificate = file_path
        instance.save()


class Video_recorderForm(forms.ModelForm):
    certificate_file = forms.FileField(label="Certificate")
    maintenance_report_file = forms.FileField(label="Maintenance_report")

    class Meta:
        model = Video_recorder
        fields = "__all__"


@admin.register(Video_recorder)
class Video_recorderAdmin(admin.ModelAdmin):
    form = Video_recorderForm

    def save_model(self, request, obj, form, change):
        certificate_file = form.cleaned_data.get("certificate_file", None)
        if certificate_file:
            obj.certificate = self.save_file(obj.pk, certificate_file)

        maintenance_report_file = form.cleaned_data.get("maintenance_report_file", None)
        if maintenance_report_file:
            obj.maintenance_report = self.save_file(obj.pk, maintenance_report_file)

        obj.save()

    @staticmethod
    def save_file(pk, file):
        file_extension = os.path.splitext(file.name)[1]

        if file.field_name == "certificate_file":
            file_path = f"Equipment/video_recorder/certificate/{pk}/{file_extension}"
        elif file.field_name == "maintenance_report_file":
            file_path = f"Equipment/video_recorder/maintenance_report/{pk}/{file_extension}"
        else:
            raise ValueError("Invalid file field")

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path


class Radio_stationForm(forms.ModelForm):
    certificate_file = forms.FileField(label="Certificate")
    maintenance_report_file = forms.FileField(label="Maintenance_report")

    class Meta:
        model = Radio_station
        fields = "__all__"


@admin.register(Radio_station)
class Radio_stationAdmin(admin.ModelAdmin):
    form = Radio_stationForm

    def save_model(self, request, obj, form, change):
        certificate_file = form.cleaned_data.get("certificate_file", None)
        if certificate_file:
            obj.certificate = self.save_file(obj.pk, certificate_file)

        maintenance_report_file = form.cleaned_data.get("maintenance_report_file", None)
        if maintenance_report_file:
            obj.maintenance_report = self.save_file(obj.pk, maintenance_report_file)

        obj.save()

    @staticmethod
    def save_file(pk, file):
        file_extension = os.path.splitext(file.name)[1]

        if file.field_name == "certificate_file":
            file_path = f"Equipment/radio_station/certificate/{pk}/{file_extension}"
        elif file.field_name == "maintenance_report_file":
            file_path = f"Equipment/radio_station/maintenance_report/{pk}/{file_extension}"
        else:
            raise ValueError("Invalid file field")

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path
