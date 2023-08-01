import os

from django.contrib import admin
from django import forms

from .models import Post, Protected_object, Client, Performer


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm



class PerformerForm(forms.ModelForm):
    file = forms.FileField(label="contract")

    class Meta:
        model = Performer
        fields = "__all__"


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    form = PerformerForm



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
