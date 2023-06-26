from django.db import models
from django.utils.translation import gettext_lazy as _

def certificate_directory_path(instance: "Armor", filename: str) -> str:
    return "certificate/certificate_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Armor(models.Model):
    class Meta:
        verbose_name = _('Armor')
        verbose_name_plural = _('Armors')

    name = models.CharField(max_length=15, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=150, null=True, blank=True, db_index=True, verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=True, blank=True, db_index=True, verbose_name=_('factory_number'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_manufacture'))
    protection_category = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('protection_category'))
    date_purchase = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_purchase'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path, verbose_name=_('foto'))


