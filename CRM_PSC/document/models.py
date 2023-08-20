from django.db import models

from typing import Union

def copy_directory_path(instance:  Union["Passport", "Driving_license", "Security_license", "Medical_certificate", "Periodic_inspection", "Electrical_certificate", "Briefing"], filename: str) -> str:
    if isinstance(instance, Passport):
        document_title = "passport"
    elif isinstance(instance, Driving_license):
        document_title = "driving_license"
    elif isinstance(instance, Security_license):
        document_title = "security_license"
    elif isinstance(instance, Medical_certificate):
        document_title = "medical_certificate"
    elif isinstance(instance, Periodic_inspection):
        document_title = "periodic_inspection"
    elif isinstance(instance, Electrical_certificate):
        document_title = "electrical_certificate"
    elif isinstance(instance, Registration_certificate):
        document_title = "registration_certificate"
    elif isinstance(instance, Vehicle_passport):
        document_title = "vehicle_passport"

    else:
        document_title = "briefing"
        return "Document/" + document_title + "/{filename}".format(
            filename=filename,
        )

    return "Document/" + document_title + "/" + instance.owner + "/{filename}".format(
        filename=filename,
    )

class Passport(models.Model):
    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, help_text="Серия и номер: 7521 123456", verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(null=True, blank=True, verbose_name='Дата окончания действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдан')
    place_registration = models.CharField(max_length=150, null=True, blank=True, verbose_name='Место прописки')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"




class Driving_license(models.Model):
    class Meta:
        verbose_name = 'Водительское удостоверение'
        verbose_name_plural = 'Водительские удостоверения'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: 7521 123456",
                                         verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(verbose_name='Дата окончания действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    driving_license_categories = models.CharField(max_length=50, null=True, blank=True, verbose_name='Разрешенные категории')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"


class Security_license(models.Model):
    class Meta:
        verbose_name = 'Удостоверение частного охранника'
        verbose_name_plural = 'Удостоверения частного охранника'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: 7521 123456",
                                         verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(verbose_name='Дата окончания действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"



class Medical_certificate(models.Model):
    class Meta:
        verbose_name = 'Медицинская справка'
        verbose_name_plural = 'Медицинские справки'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: 7521 123456",
                                         verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(verbose_name='Дата окончания действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"




class Periodic_inspection(models.Model):
    class Meta:
        verbose_name = 'Периодическая проверка'
        verbose_name_plural = 'Периодические проверки'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: 7521 123456",
                                         verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(verbose_name='Дата окончания действия')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"


class Electrical_certificate(models.Model):
    class Meta:
        verbose_name = 'Удостоверение по ЭБ'
        verbose_name_plural = 'Удостоверения по ЭБ'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, help_text="Серия и номер: 7521 123456",
                                         verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    test_date = models.DateField(verbose_name='Дата проверки')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"




class Vehicle_passport(models.Model):
    class Meta:
        verbose_name = 'Паспорт ТС'
        verbose_name_plural = 'Паспорта ТС'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    VIN_number = models.CharField(max_length=20, verbose_name='VIN номер')
    license_plate = models.CharField(max_length=10, help_text="Формат: У174ТВ774", verbose_name='Номерной знак')
    series_and_number = models.CharField(max_length=30, help_text="Серия и номер: 7521 123456", verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.license_plate}"





class Registration_certificate(models.Model):
    class Meta:
        verbose_name = 'Свидетельство о регистрации ТС'
        verbose_name_plural = 'Свидетельства о регистрации ТС'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    license_plate = models.CharField(max_length=10, help_text="Формат: У174ТВ774", verbose_name='Номерной знак')
    name = models.CharField(max_length=20, verbose_name='Марка автомобиля')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: 7521 123456", verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)
    def __str__(self):
        return f"{self.license_plate}"



class Insurance_policy(models.Model):
    class Meta:
        verbose_name = 'Страховой полис'
        verbose_name_plural = 'Страховые полисы'

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    vehicle = models.CharField(max_length=20, verbose_name='Марка автомобиля')
    license_plate = models.CharField(max_length=10, help_text="Формат: У174ТВ774", verbose_name='Номерной знак')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text="Серия и номер: ААА 123456", verbose_name='Серия и номер')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    date_expiration = models.DateField(verbose_name='Дата окончания действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')

    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)
    def __str__(self):
        return f"{self.license_plate}"

class Briefing(models.Model):
    class Meta:
        verbose_name = 'Инструктаж'
        verbose_name_plural = 'Инструктажи'

    owner = models.CharField(max_length=30, help_text="Например: Охрана труда", verbose_name='Дисциплина')
    description = models.TextField(verbose_name='Описание')
    data_briefing = models.DateField(verbose_name='Дата инструктажа')
    data_briefing_next = models.DateField(verbose_name='Дата следующего инструктажа')
    committee_chair = models.CharField(max_length=30, verbose_name='Кто проводил')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.name!r}, data: {self.data_briefing}"
