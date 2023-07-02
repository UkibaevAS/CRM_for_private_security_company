import os

from django.contrib import admin
from django import forms

from .models import Security_system, Alarm_system, Webcam


class Security_systemForm(forms.ModelForm):
    certificate_file = forms.FileField(label="Certificate")
    maintenance_report_file = forms.FileField(label="Maintenance_report")
    installation_report_file = forms.FileField(label="installation_report")

    class Meta:
        model = Security_system
        fields = "__all__"


@admin.register(Security_system)
class Security_systemAdmin(admin.ModelAdmin):
    form = Security_systemForm

    def save_model(self, request, obj, form, change):
        certificate_file = form.cleaned_data.get("certificate_file", None)
        if certificate_file:
            obj.certificate = self.save_file(obj.pk, certificate_file)

        maintenance_report_file = form.cleaned_data.get("maintenance_report_file", None)
        if maintenance_report_file:
            obj.maintenance_report = self.save_file(obj.pk, maintenance_report_file)

        installation_report_file = form.cleaned_data.get("installation_report_file", None)
        if installation_report_file:
            obj.installation_report = self.save_file(obj.pk, installation_report_file)

        obj.save()

    @staticmethod
    def save_file(pk, file):
        file_extension = os.path.splitext(file.name)[1]

        if file.field_name == "certificate_file":
            file_path = f"Security_system/security_system/certificate/{pk}/{file_extension}"
        elif file.field_name == "maintenance_report_file":
            file_path = f"Security_system/security_system/maintenance_report/{pk}/{file_extension}"
        elif file.field_name == "installation_report_file":
            file_path = f"Security_system/security_system/maintenance_report/{pk}/{file_extension}"
        else:
            raise ValueError("Invalid file field")

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path


class Alarm_systemForm(forms.ModelForm):
    certificate_file = forms.FileField(label="Certificate")
    maintenance_report_file = forms.FileField(label="Maintenance_report")
    installation_report_file = forms.FileField(label="installation_report")

    class Meta:
        model = Alarm_system
        fields = "__all__"


@admin.register(Alarm_system)
class Alarm_systemAdmin(admin.ModelAdmin):
    form = Alarm_systemForm

    def save_model(self, request, obj, form, change):
        certificate_file = form.cleaned_data.get("certificate_file", None)
        if certificate_file:
            obj.certificate = self.save_file(obj.pk, certificate_file)

        maintenance_report_file = form.cleaned_data.get("maintenance_report_file", None)
        if maintenance_report_file:
            obj.maintenance_report = self.save_file(obj.pk, maintenance_report_file)

        installation_report_file = form.cleaned_data.get("installation_report_file", None)
        if installation_report_file:
            obj.installation_report = self.save_file(obj.pk, installation_report_file)

        obj.save()

    @staticmethod
    def save_file(pk, file):
        file_extension = os.path.splitext(file.name)[1]

        if file.field_name == "certificate_file":
            file_path = f"Security_system/alarm_system/certificate/{pk}/{file_extension}"
        elif file.field_name == "maintenance_report_file":
            file_path = f"Security_system/alarm_system/maintenance_report/{pk}/{file_extension}"
        elif file.field_name == "installation_report_file":
            file_path = f"Security_system/alarm_system/maintenance_report/{pk}/{file_extension}"
        else:
            raise ValueError("Invalid file field")

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path


class WebcamForm(forms.ModelForm):
    certificate_file = forms.FileField(label="Certificate")
    maintenance_report_file = forms.FileField(label="Maintenance_report")
    installation_report_file = forms.FileField(label="installation_report")

    class Meta:
        model = Webcam
        fields = "__all__"


@admin.register(Webcam)
class WebcamAdmin(admin.ModelAdmin):
    form = WebcamForm

    def save_model(self, request, obj, form, change):
        certificate_file = form.cleaned_data.get("certificate_file", None)
        if certificate_file:
            obj.certificate = self.save_file(obj.pk, certificate_file)

        maintenance_report_file = form.cleaned_data.get("maintenance_report_file", None)
        if maintenance_report_file:
            obj.maintenance_report = self.save_file(obj.pk, maintenance_report_file)

        installation_report_file = form.cleaned_data.get("installation_report_file", None)
        if installation_report_file:
            obj.installation_report = self.save_file(obj.pk, installation_report_file)

        obj.save()

    @staticmethod
    def save_file(pk, file):
        file_extension = os.path.splitext(file.name)[1]

        if file.field_name == "certificate_file":
            file_path = f"Security_system/webcam/certificate/{pk}/{file_extension}"
        elif file.field_name == "maintenance_report_file":
            file_path = f"Security_system/webcam/maintenance_report/{pk}/{file_extension}"
        elif file.field_name == "installation_report_file":
            file_path = f"Security_system/webcam/maintenance_report/{pk}/{file_extension}"
        else:
            raise ValueError("Invalid file field")

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path
