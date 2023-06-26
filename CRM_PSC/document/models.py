from django.db import models
from django.utils.translation import gettext_lazy as _


def document_directory_path(instance: "Document", filename: str) -> str:
    return "document/document_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def briefing_report_directory_path(instance: "Briefing", filename: str) -> str:
    return "briefing/briefing_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Document(models.Model):
    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name_document'))
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("format: series number"),
                                         verbose_name=_('series_and_number_document'))
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_issue_document'))
    date_expiration = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"),
                                       verbose_name=_('date_expiration_document'))
    who_issued = models.CharField(max_length=50, null=False, blank=False, db_index=True,
                                  verbose_name=_('who_issued_document'))
    place_registration = models.CharField(max_length=150, null=False, blank=False, db_index=True,
                                          verbose_name=_('place_registration_document'))
    driving_license_categories = models.CharField(max_length=150, null=False, blank=True, db_index=True,
                                                  verbose_name=_('driving_license_categories_document'))
    document_copy = models.ImageField(null=True, blank=True, upload_to=document_directory_path,
                                      verbose_name=_('document_copy'))

    def __str__(self):
        return f"{_('Document')}(pk={self.pk}, name={self.name!r})"


class Briefing(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name_briefing'))
    description = models.TextField(null=False, blank=False, db_index=True, verbose_name=_('description_briefing'))
    data_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_briefing'))
    committee_chair = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                       verbose_name=_('committee_chair'))
    briefing_report = models.ImageField(null=True, blank=True, upload_to=briefing_report_directory_path,
                                        verbose_name=_('briefing_report'))
    data_next_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                          help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_next_briefing'))

    def __str__(self):
        return f"{_('Briefing')}(pk={self.pk}, name={self.name!r})"
