from django.db import models
from django.utils.translation import gettext_lazy as _


def copy_directory_path(instance:  "Affiliated_company", filename: str) -> str:

    return "Affiliated_company/" + instance.name + "/{filename}".format(
        filename=filename,
    )

class Affiliated_company(models.Model):
    class Meta:
        verbose_name = 'Аффилированная (дочерняя) компания'
        verbose_name_plural = 'Аффилированные (дочернии) компании'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.PositiveBigIntegerField(default=0, help_text=_("Формат: 83517772233"), verbose_name='Телефон')
    email = models.EmailField(max_length=100, null=True, blank=True)
    INN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='ИНН')
    OGRN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='OGRN')
    EGRUL = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='ЕГРЮЛ/ЕГРИП')
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name='Банковсие реквизиты')
    director = models.CharField(max_length=75, verbose_name='Директор')
    contact_person = models.CharField(max_length=75, verbose_name='Контактное лицо')
    phone_contact_person = models.PositiveBigIntegerField(default=0, help_text=_("Формат: 83517772233"),
                                                          verbose_name=_('Телефон контактного лица'))
    contract = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Договор о сотрудничестве')

    def __str__(self):
        return f"{self.name}"

class Department(models.Model):
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    name = models.CharField(max_length=50, verbose_name='Название')
    manager = models.CharField(max_length=75, verbose_name='Начальник')

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return f"{self.name}"