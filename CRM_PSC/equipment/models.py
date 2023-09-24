from django.db import models

from structure_of_company.models import Affiliated_company
from typing import Union


def copy_directory_path(instance: Union[
    "Uniform",
    "Gun",
    "Handcuffs",
    "Rubber_stick",
    "Special_spray",
    "Armor",
    "Video_recorder",
    "Radio_station"
],
                        filename: str) -> str:
    if isinstance(instance, Uniform):
        document_title = "uniform"
    elif isinstance(instance, Gun):
        document_title = "gun"
    elif isinstance(instance, Handcuffs):
        document_title = "handcuffs"
    elif isinstance(instance, Rubber_stick):
        document_title = "rubber_stick"
    elif isinstance(instance, Special_spray):
        document_title = "special_spray"
    elif isinstance(instance, Armor):
        document_title = "armor"
    elif isinstance(instance, Video_recorder):
        document_title = "video_recorder"
    else:
        document_title = "radio_station"

    return "Equipment/" + document_title + "/certificate/{filename}".format(
        filename=filename,
    )


def copy_report_directory_path(instance: Union["Video_recorder", "Radio_station"], filename: str) -> str:
    if isinstance(instance, Video_recorder):
        document_title = "video_recorder"
    else:
        document_title = "radio_station"
    return "Equipment/" + document_title + "/maintenance_report/{filename}".format(
        filename=filename,
    )

class Equipment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Числится на балансе')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    date_manufacture = models.DateField(null=True, blank=True, verbose_name='Дата производства')
    certificate = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Паспорт')


class Uniform(models.Model):
    class Meta:
        verbose_name = 'Униформа'
        verbose_name_plural = 'Униформа'

    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Числится на балансе')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    size = models.SmallIntegerField(default=0, verbose_name='Размер')


    def __str__(self):
        return f"{self.name}, 'size' - {self.size}"



class Gun(Equipment):
    class Meta:
        verbose_name = 'Вооружение'
        verbose_name_plural = 'Вооружение'

    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    date_test_shoot = models.DateField(null=True, blank=True, verbose_name='Дата контрольного отстрела')

    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"



class Handcuffs(Equipment):
    class Meta:
        verbose_name = 'Наручники'
        verbose_name_plural = 'Наручники'

    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')

    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"



class Rubber_stick(Equipment):
    class Meta:
        verbose_name = 'Палка резиновая'
        verbose_name_plural = 'Палка резиновая'

    def __str__(self):
        return f"{self.name}, дата поступления: {self.receipt_date}"



class Special_spray(Equipment):
    class Meta:
        verbose_name = 'Аэрозоль специальный'
        verbose_name_plural = 'Аэрозоли специальные'

    expiration_date = models.DateField(verbose_name='Годен до')

    def __str__(self):
        return f"{self.name}, дата поступления: {self.receipt_date}"


class Armor(Equipment):
    class Meta:
        verbose_name = 'Бронезащита'
        verbose_name_plural = 'Бронезащита'

    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    protection_category = models.SmallIntegerField(default=1, null=True, blank=True, verbose_name='Класс защиты')

    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"



class Video_recorder(Equipment):
    class Meta:
        verbose_name = 'Видеорегистратор'
        verbose_name_plural = 'Видеорегистраторы'

    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    installation_date = models.DateField(null=True, blank=True, verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, help_text="Количество месяцев: XX", verbose_name='Периодичность ТО')
    service_date = models.DateField(null=True, blank=True, verbose_name='Дата проведенного ТО')
    service_date_next = models.DateField(null=True, blank=True, verbose_name='Дата следующего ТО')
    maintenance_report = models.FileField(null=True, blank=True, upload_to=copy_report_directory_path,
                                          verbose_name='Акт о проведенном ТО')
    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"



class Radio_station(Equipment):
    class Meta:
        verbose_name = 'Радиостанция'
        verbose_name_plural = 'Радиостанции'

    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    installation_date = models.DateField(null=True, blank=True, verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False,help_text="Количество месяцев: XX",
                                            verbose_name='Периодичность ТО')
    service_date = models.DateField(null=True, blank=True, verbose_name='Дата проведенного ТО')
    service_date_next = models.DateField(null=True, blank=True, verbose_name='Дата следующего ТО')
    maintenance_report = models.FileField(null=True, blank=True, upload_to=copy_report_directory_path,
                                          verbose_name='Акт о проведенном ТО')
    def __str__(self):
        return f"{self.name}, Зав.№:{self.factory_number}"

