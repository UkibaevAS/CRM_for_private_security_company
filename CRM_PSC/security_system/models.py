from django.db import models

from config.models import Affiliated_company
from typing import Union


def copy_certificate_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"], filename: str) -> str:
    if isinstance(instance, Security_system):
        document_title = "security_system"
    elif isinstance(instance, Alarm_system):
        document_title = "alarm_system"
    else:
        document_title = "webcam"
    return "Security_system/" + document_title + "/certificate/{filename}".format(
        filename=filename,
    )

def copy_maintenance_report_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"], filename: str) -> str:
    if isinstance(instance, Security_system):
        document_title = "security_system"
    elif isinstance(instance, Alarm_system):
        document_title = "alarm_system"
    else:
        document_title = "webcam"
    return "Security_system/" + document_title + "/maintenance_report/{filename}".format(
        filename=filename,
    )

def copy_installation_report_directory_path(instance: Union["Security_system", "Alarm_system", "Webcam"], filename: str) -> str:
    if isinstance(instance, Security_system):
        document_title = "security_system"
    elif isinstance(instance, Alarm_system):
        document_title = "alarm_system"
    else:
        document_title = "webcam"
    return "Security_system/" + document_title + "/installation_report/{filename}".format(
        filename=filename,
    )

class Security_system(models.Model):
    class Meta:
        verbose_name = 'Охранная система'
        verbose_name_plural = 'Охранные системы'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Числится на балансе')
    installation_date = models.DateField(null=True, blank=True, verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            help_text="Количество месяцев: XX", verbose_name='Периодичность ТО')
    date_manufacture = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата производства')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    service_date = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата проведенного ТО')
    service_date_next = models.DateField(null=True, blank=True, verbose_name='Дата следующего ТО')
    certificate = models.FileField(null=True, blank=True, upload_to=copy_certificate_directory_path, verbose_name='Паспорт')
    maintenance_report = models.FileField(null=True, blank=True, upload_to=copy_maintenance_report_directory_path,
                                          verbose_name='Акт о проведенном ТО')
    installation_report = models.FileField(null=True, blank=True, upload_to=copy_installation_report_directory_path,
                                          verbose_name='Акт установки')

    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"

class Alarm_system(models.Model):
    class Meta:
        verbose_name = 'Система сигнализации'
        verbose_name_plural = 'Системы сигнализации'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Числится на балансе')
    installation_date = models.DateField(null=True, blank=True, verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            help_text="Количество месяцев: XX", verbose_name='Периодичность ТО')
    date_manufacture = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата производства')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    service_date = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата проведенного ТО')
    service_date_next = models.DateField(null=True, blank=True, verbose_name='Дата следующего ТО')
    certificate = models.FileField(null=True, blank=True, upload_to=copy_certificate_directory_path, verbose_name='Паспорт')
    maintenance_report = models.FileField(null=True, blank=True, upload_to=copy_maintenance_report_directory_path,
                                          verbose_name='Акт о проведенном ТО')
    installation_report = models.FileField(null=True, blank=True, upload_to=copy_installation_report_directory_path,
                                           verbose_name='Акт установки')
    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"

class Webcam(models.Model):
    class Meta:
        verbose_name = 'Видеокамера'
        verbose_name_plural = 'Видеокамеры'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Числится на балансе')
    installation_date = models.DateField(null=True, blank=True, verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            help_text="Количество месяцев: XX", verbose_name='Периодичность ТО')
    date_manufacture = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата производства')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    service_date = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата проведенного ТО')
    service_date_next = models.DateField(null=True, blank=True, verbose_name='Дата следующего ТО')
    certificate = models.FileField(null=True, blank=True, upload_to=copy_certificate_directory_path, verbose_name='Паспорт')
    maintenance_report = models.FileField(null=True, blank=True, upload_to=copy_maintenance_report_directory_path,
                                          verbose_name='Акт о проведенном ТО')
    installation_report = models.FileField(null=True, blank=True, upload_to=copy_installation_report_directory_path,
                                           verbose_name='Акт установки')
    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"
