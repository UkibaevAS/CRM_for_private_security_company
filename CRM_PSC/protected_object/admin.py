import os

from django.contrib import admin
from django import forms

from .models import Post, Protected_object, Client, Performer


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "name", "phone"
    list_display_links = "name",
    ordering = "-name",
    search_fields = "name", "phone"
    fieldsets = [
        (None, {
            "fields": (
                "name", "protection_mode", "start_day_shift", "start_day_shift_free_day", "start_night_shift", "phone",
                "number_per_day", "number_per_night", "armors", "guns", "radio_stations", "webcams", "performer",
                "alarm_systems", "vehicles",
            ),
        }),
    ]


class ClientForm(forms.ModelForm):
    file = forms.FileField(label="contract")

    class Meta:
        model = Client
        fields = "__all__"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Client/contracts/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.contract = file_path
        instance.save()


class PerformerForm(forms.ModelForm):
    file = forms.FileField(label="contract")

    class Meta:
        model = Performer
        fields = "__all__"


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    form = PerformerForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Performer/contracts/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.contract = file_path
        instance.save()


class Protected_objectForm(forms.ModelForm):
    file = forms.FileField(label="foto")

    class Meta:
        model = Protected_object
        fields = "__all__"


@admin.register(Protected_object)
class Protected_objectAdmin(admin.ModelAdmin):
    form = Protected_objectForm

    def save_file(instance, file):
        file_extension = os.path.splitext(file.name)[1]

        file_path = "Protected_object/foto/{pk}/{filename}".format(pk=instance.pk, extension=file_extension)

        with open(file_path, "wb") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        instance.foto = file_path
        instance.save()
