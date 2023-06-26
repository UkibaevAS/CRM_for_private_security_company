from django.contrib import admin

from .models import Document, Briefing


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = "name", "driving_license_categories"
    list_display_links = "name", "driving_license_categories"
    ordering = ("-name",)
    search_fields = "name", "driving_license_categories"
    fieldsets = [
        (None, {
            "fields": ("name", "series_and_number", "date_issue", "date_expiration", "who_issued", "place_registration",
                       "place_of_residence", "driving_license_categories", "document_copy",
                       ),
        }),
    ]


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
