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

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_security_system'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_security_system'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number_security_system'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_security_system'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date_security_system'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report_security_system'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval_security_system'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture_security_system'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date_security_system'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date_security_system'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_security_system'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report_security_system'))


class Alarm_system(models.Model):
    class Meta:
        verbose_name = _('Alarm_system')
        verbose_name_plural = _('Alarm_systems')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_alarm_system'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_alarm_system'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number_alarm_system'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_alarm_system'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date_alarm_system'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report_alarm_system'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval_alarm_system'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture_alarm_system'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date_alarm_system'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('service_date_alarm_system'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next_alarm_system'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report_alarm_system'))


class Webcam(models.Model):
    class Meta:
        verbose_name = _('Webcam')
        verbose_name_plural = _('Webcams')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_webcam'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_webcam'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number_webcam'))
    certificate = models.ImageField(null=True, blank=True, upload_to=certificate_directory_path,
                                    verbose_name=_('certificate_webcam'))
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date_webcam'))
    installation_report = models.ImageField(null=True, blank=True, upload_to=installation_report_directory_path,
                                            verbose_name=_('installation_report_webcam'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            verbose_name=_('maintenance_interval_webcam'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture_webcam'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date_webcam'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('service_date_webcam'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next_webcam'))
    maintenance_report = models.ImageField(null=True, blank=True, upload_to=maintenance_report_directory_path,
                                           verbose_name=_('maintenance_report_webcam'))
