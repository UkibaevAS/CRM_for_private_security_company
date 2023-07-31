from django.db import models
from django.utils.translation import gettext_lazy as _

from typing import Union

def copy_directory_path(instance:  Union["Passport", "Driving_license", "Security_license", "Medical_certificate", "Periodic_inspection", "Briefing"], filename: str) -> str:
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
    else:
        document_title = "briefing"

    #print(instance.name)
    return "Document/" + document_title + "/" + instance.owner + "/{filename}".format(
        filename=filename,
    )

class Passport(models.Model):
    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

    owner = models.CharField(max_length=30, db_index=True,
                            verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("Формат: dd.mm.yyyy"),
                                       verbose_name='Срок действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                  verbose_name='Кем выдан')
    place_registration = models.CharField(max_length=150, null=True, blank=True, db_index=True,
                                          verbose_name='Место прописки')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"




class Driving_license(models.Model):
    class Meta:
        verbose_name = 'Водительское удостоверение'
        verbose_name_plural = 'Водительские удостоверения'

    owner = models.CharField(max_length=30, db_index=True,
                             verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("Формат: dd.mm.yyyy"),
                                       verbose_name='Срок действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                  verbose_name='Кем выдано')
    driving_license_categories = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                                  verbose_name=_('Разрешенные категории'))
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"


class Security_license(models.Model):
    class Meta:
        verbose_name = 'Удостоверение частного охранника'
        verbose_name_plural = 'Удостоверения частного охранника'

    owner = models.CharField(max_length=30, db_index=True,
                             verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("Формат: dd.mm.yyyy"),
                                       verbose_name='Срок действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                  verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"



class Medical_certificate(models.Model):
    class Meta:
        verbose_name = 'Медицинская справка'
        verbose_name_plural = 'Медицинские справки'

    owner = models.CharField(max_length=30, db_index=True,
                             verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("Формат: dd.mm.yyyy"),
                                       verbose_name='Срок действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кем выдано')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"




class Periodic_inspection(models.Model):
    class Meta:
        verbose_name = 'Периодическая проверка'
        verbose_name_plural = 'Периодические проверки'

    owner = models.CharField(max_length=30, db_index=True,
                             verbose_name='Владелец')
    series_and_number = models.CharField(max_length=30, null=False, blank=False, help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Копия')

    def __str__(self):
        return f"{self.owner}"


class Briefing(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name'))
    description = models.TextField(null=False, blank=False, db_index=True, verbose_name=_('description'))
    data_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data'))
    committee_chair = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                       verbose_name=_('committee_chair'))
    data_next_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                          help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_next'))
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.name!r}, {_('data')}={self.data_briefing})"


class Document(models.Model):
    class Meta:
        verbose_name = 'Водительское удостоверение'
        verbose_name_plural = 'Водительские удостоверения'

    owner = models.CharField(max_length=30, db_index=True,
                             verbose_name='Владелец')
    sseries_and_number = models.CharField(max_length=30, null=False, blank=False, db_index=True,
                                         help_text=_("Серия и номер: 7521 123456"),
                                         verbose_name='Серия и номер')
    date_issue = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("Формат: dd.mm.yyyy"), verbose_name='Дата выдачи')
    date_expiration = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("Формат: dd.mm.yyyy"),
                                       verbose_name='Срок действия')
    who_issued = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                  verbose_name='Кем выдано')
    driving_license_categories = models.CharField(max_length=50, null=True, blank=True, db_index=True,
                                                  verbose_name=_('Разрешенные категории'))
    copy = models.FileField(null=True, blank=True, upload_to=copy_directory_path)

    def __str__(self):
        return f"{self.owner!r}"
