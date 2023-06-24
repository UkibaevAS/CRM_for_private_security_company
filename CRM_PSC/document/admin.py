from django.contrib import admin

from .models import Document


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
