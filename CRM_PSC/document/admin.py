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

    def save_file(instance, file):
        # Получение расширения файла
        file_extension = os.path.splitext(file.name)[1]

        # Создание пути сохранения файла
        file_path = "Document/document/{pk}/{filename}".format(
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
    file = forms.FileField(label="Briefing_copy")

    class Meta:
        model = Briefing
        fields = "__all__"


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    form = BriefingForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Document/briefing/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.briefing_copy = file_path
        instance.save()
