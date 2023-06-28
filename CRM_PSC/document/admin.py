import os

from django.contrib import admin
from django import forms

from .models import Document, Briefing


class DocumentForm(forms.ModelForm):
    file = forms.FileField(label="Document_copy")

    class Meta:
        model = Document
        fields = "__all__"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm

    # def save_model(self, request, obj, form, change):
    #     pdf_file = form.cleaned_data.get("pdf_file", None)
    #     if pdf_file:
    #         obj.document_copy.save(pdf_file.name, pdf_file)
    #     obj.save()
def save_file(instance, file):
    # Получение расширения файла
    file_extension = os.path.splitext(file.name)[1]

    # Создание пути сохранения файла
    file_path = "document/document_{pk}/{filename}".format(
        pk=instance.pk,
        extension=file_extension
    )

    # Открытие файла и сохранение его контента в атрибут document_copy
    with open(file_path, "wb") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    # Сохранение пути файла в атрибут document_copy
    instance.document_copy = file_path
    instance.save()

class BriefingForm(forms.ModelForm):
    pdf_file = forms.FileField(label="Briefing_report_PDF")

    class Meta:
        model = Briefing
        fields = "__all__"


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    form = BriefingForm

    def save_model(self, request, obj, form, change):
        pdf_file = form.cleaned_data.get("pdf_file", None)
        if pdf_file:
            obj.document_copy.save(pdf_file.name, pdf_file)
        obj.save()
