from django.contrib import admin
from django.core.files import File
from django.db.models import QuerySet
from django.http import HttpRequest
import os

from django.contrib import admin
from django import forms

from .models import Worker


@admin.action(description="Archive worker")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive worker")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)





class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = "__all__"


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    form = WorkerForm
    ordering = ['second_name']
    actions = [
        mark_archived,
        mark_unarchived,
    ]

