from django.db import models
from django.utils.translation import gettext_lazy as _


def certificate_directory_path(instance: "Gun", filename: str) -> str:
    return "certificate/certificate_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Gun(models.Model):
    class Meta:
        verbose_name = _('Gun')
        verbose_name_plural = _('Guns')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True, verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True, verbose_name=_('factory_number'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_manufacture'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path, verbose_name=_('certificate'))
    date_test_shoot = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_test_shoot'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))

