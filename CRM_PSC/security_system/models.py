from typing import Union

from django.db import models
from django.utils.translation import gettext_lazy as _


def certificate_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"], filename: str) -> str:
    return "certificate_security_system/certificate_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def maintenance_report_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"],
                                      filename: str) -> str:
    return "maintenance_report_security_system/maintenance_report_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def installation_report_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"],
                                       filename: str) -> str:
    return "installation_report_security_system/installation_report_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Security_system(models.Model):
    class Meta:
        verbose_name = _('Security_system')
        verbose_name_plural = _('Security_systems')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report'))


class Alarm_system(models.Model):
    class Meta:
        verbose_name = _('Alarm_system')
        verbose_name_plural = _('Alarm_systems')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('service_date'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report'))


class Webcam(models.Model):
    class Meta:
        verbose_name = _('Webcam')
        verbose_name_plural = _('Webcams')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_webcam'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('service_date'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report'))
