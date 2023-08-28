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
    class Meta:
        model = Performer
        fields = "__all__"


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    form = PerformerForm
    ordering = ['name']



class Protected_objectForm(forms.ModelForm):
    class Meta:
        model = Protected_object
        fields = "__all__"


@admin.register(Protected_object)
class Protected_objectAdmin(admin.ModelAdmin):
    form = Protected_objectForm
    ordering = ['name']
