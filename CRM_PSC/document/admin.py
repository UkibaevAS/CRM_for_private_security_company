import os

from django.contrib import admin
from django import forms

from .models import Document, Briefing


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = "__all__"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm



class BriefingForm(forms.ModelForm):

    class Meta:
        model = Briefing
        fields = "__all__"


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    form = BriefingForm


