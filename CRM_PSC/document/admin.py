import os

from django.contrib import admin
from django import forms

from .models import Passport, Driving_license, Briefing, Security_license, Medical_certificate, Periodic_inspection, \
    Electrical_certificate, Registration_certificate, Vehicle_passport, Insurance_policy


class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = "__all__"


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    form = PassportForm


class Driving_licenseForm(forms.ModelForm):
    class Meta:
        model = Driving_license
        fields = "__all__"


@admin.register(Driving_license)
class DocumentAdmin(admin.ModelAdmin):
    form = Driving_licenseForm


class Security_licenseForm(forms.ModelForm):
    class Meta:
        model = Security_license
        fields = "__all__"


@admin.register(Security_license)
class Security_licenseAdmin(admin.ModelAdmin):
    form = Security_licenseForm


class Medical_certificateForm(forms.ModelForm):
    class Meta:
        model = Medical_certificate
        fields = "__all__"


@admin.register(Medical_certificate)
class Medical_certificateAdmin(admin.ModelAdmin):
    form = Medical_certificateForm


class Periodic_inspectionForm(forms.ModelForm):
    class Meta:
        model = Periodic_inspection
        fields = "__all__"


@admin.register(Periodic_inspection)
class Periodic_inspectionAdmin(admin.ModelAdmin):
    form = Periodic_inspectionForm


class Electrical_certificateForm(forms.ModelForm):
    class Meta:
        model = Electrical_certificate
        fields = "__all__"


@admin.register(Electrical_certificate)
class Electrical_certificateAdmin(admin.ModelAdmin):
    form = Electrical_certificateForm


class Registration_certificateForm(forms.ModelForm):
    class Meta:
        model = Registration_certificate
        fields = "__all__"


@admin.register(Registration_certificate)
class Registration_certificateAdmin(admin.ModelAdmin):
    form = Registration_certificateForm


class Vehicle_passportForm(forms.ModelForm):
    class Meta:
        model = Vehicle_passport
        fields = "__all__"


@admin.register(Vehicle_passport)
class Vehicle_passportAdmin(admin.ModelAdmin):
    form = Vehicle_passportForm


class Insurance_policyForm(forms.ModelForm):
    class Meta:
        model = Insurance_policy
        fields = "__all__"


@admin.register(Insurance_policy)
class Insurance_policyAdmin(admin.ModelAdmin):
    form = Insurance_policyForm


class BriefingForm(forms.ModelForm):
    class Meta:
        model = Briefing
        fields = "__all__"


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    form = BriefingForm
