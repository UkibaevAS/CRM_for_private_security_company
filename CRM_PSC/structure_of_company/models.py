from django.db import models

from CRM_PSC.protected_object.models import Organization


def copy_directory_path(instance: "Affiliated_company", filename: str) -> str:
    return "Affiliated_company/" + instance.name + "/{filename}".format(
        filename=filename,
    )


class Affiliated_company(Organization):
    class Meta:
        verbose_name = 'Аффилированная (дочерняя) компания'
        verbose_name_plural = 'Аффилированные (дочернии) компании'

    INN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='ИНН')
    OGRN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='ОГРН')
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name='Банковские реквизиты')
    contract = models.FileField(null=True, blank=True, upload_to=copy_directory_path,
                                verbose_name='Договор об оказании услуг')


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
