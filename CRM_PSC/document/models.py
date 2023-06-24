from django.db import models
from django.utils.translation import gettext_lazy as _

def document_directory_path(instance: "Document", filename: str) -> str:
    return "document/document_{pk}/copy/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Document(models.Model):
    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name'))
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True, verbose_name=_('series_and_number'))
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True, verbose_name=_('date_issue'))
    date_expiration = models.CharField(max_length=10, null=False, blank=False, db_index=True, verbose_name=_('date_expiration'))
    who_issued = models.CharField(max_length=50, null=False, blank=False, db_index=True, verbose_name=_('who_issued'))
    place_registration = models.CharField(max_length=150, null=False, blank=False, db_index=True, verbose_name=_('place_registration'))
    place_of_residence = models.CharField(max_length=150, null=False, blank=False, db_index=True, verbose_name=_('place_of_residence'))
    driving_license_categories = models.CharField(max_length=150, null=False, blank=True, db_index=True, verbose_name=_('driving_license_categories'))
    document_copy = models.ImageField(null=True, blank=True, upload_to=document_directory_path, verbose_name=_('document_copy'))

    def __str__(self):
        return f"{_('Document')}(pk={self.pk}, name={self.name!r})"
