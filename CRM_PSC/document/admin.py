import os

from django.contrib import admin
from django import forms

from .models import Passport, Driving_license, Briefing, Security_license, Medical_certificate, Periodic_inspection


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





class BriefingForm(forms.ModelForm):

    class Meta:
        model = Briefing
        fields = "__all__"


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    form = BriefingForm


