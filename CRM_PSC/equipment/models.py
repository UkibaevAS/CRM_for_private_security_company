from typing import Union

from django.db import models
from django.utils.translation import gettext_lazy as _


def certificate_directory_path(instance: Union["Gun", "Armor"], filename: str) -> str:
    return "certificate_equipment/certificate_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def maintenance_report_directory_path(instance: Union["Video_recorder"], filename: str) -> str:
    return "maintenance_report_equipment/maintenance_report_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Uniform(models.Model):
    class Meta:
        verbose_name = _('Uniform')
        verbose_name_plural = _('Uniforms')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name_uniform'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_uniform'))
    size = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('size_uniform'))

    def __str__(self):
        return f"{_('Uniform')}(pk={self.pk}, name={self.name!r})"


class Gun(models.Model):
    class Meta:
        verbose_name = _('Gun')
        verbose_name_plural = _('Guns')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_gun'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_gun'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number_gun'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_manufacture_gun'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_gun'))
    date_test_shoot = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_test_shoot'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date_gun'))


class Armor(models.Model):
    class Meta:
        verbose_name = _('Armor')
        verbose_name_plural = _('Armors')

    name = models.CharField(max_length=15, db_index=True, verbose_name=_('name_armor'))
    description = models.CharField(max_length=150, null=True, blank=True, db_index=True,
                                   verbose_name=_('description_armor'))
    factory_number = models.CharField(max_length=15, null=True, blank=True, db_index=True,
                                      verbose_name=_('factory_number_armor'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture_armor'))
    protection_category = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True,
                                                   verbose_name=_('protection_category_armor'))
    date_purchase = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_purchase_armor'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_armor'))


class Video_recorder(models.Model):
    class Meta:
        verbose_name = _('Video_recorder')
        verbose_name_plural = _('Video_recorders')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_video_recorder'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_video_recorder'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number_video_recorder'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_video_recorder'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date_video_recorder'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval_video_recorder'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture_video_recorder'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date_video_recorder'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date_video_recorder'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next_video_recorder'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report_video_recorder'))
