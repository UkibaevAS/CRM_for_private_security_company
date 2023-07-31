from django.db import models
from django.utils.translation import gettext_lazy as _

from typing import Union

def copy_directory_path(instance:  Union["Document", "Briefing"], filename: str) -> str:
    if isinstance(instance, Document):
        document_title = "document"
    else:
        document_title = "briefing"

    print(instance.name)
    return "Document/" + document_title + "/" + instance.name + "/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Document(models.Model):
    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    name = models.CharField(max_length=30, db_index=True,
                            verbose_name=_('name'))  # выбор из возможных вариантов (список)
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("format: series number"),
                                         verbose_name=_('series_and_number'))
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_issue'))
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"),
                                       verbose_name=_('date_expiration'))
    who_issued = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                  verbose_name=_('who_issued'))
    place_registration = models.CharField(max_length=150, null=True, blank=True, db_index=True,
                                          verbose_name=_('place_registration'))
    driving_license_categories = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                                  verbose_name=_('driving_license_categorie'))
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.name!r}"


class Briefing(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name'))
    description = models.TextField(null=False, blank=False, db_index=True, verbose_name=_('description'))
    data_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data'))
    committee_chair = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                       verbose_name=_('committee_chair'))
    data_next_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                          help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_next'))
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.name!r}, {_('data')}={self.data_briefing})"
