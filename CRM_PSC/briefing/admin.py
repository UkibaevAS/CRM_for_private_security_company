from django.contrib import admin

from .models import Briefing


@admin.register(Briefing)
class BriefingAdmin(admin.ModelAdmin):
    list_display = "name", "description"
    list_display_links = "name", "description"
    ordering = "-name", "description"
    search_fields = "-name", "description", "data_briefing"
    fieldsets = [
        (None, {
            "fields": ("name", "description", "data_briefing", "committee_chair", "briefing_report",
                       "data_next_briefing",
                       ),
        }),
    ]
