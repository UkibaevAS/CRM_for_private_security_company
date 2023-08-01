from django.db import models


from config.models import Affiliated_company, Department, Position
from document.models import Passport, Driving_license, Security_license, Medical_certificate, Periodic_inspection, Electrical_certificate, Briefing
from equipment.models import Uniform




def photo_directory_path(instance: "Worker", filename: str) -> str:
    return "Worker/photo/{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Worker(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    second_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    photo = models.ImageField(null=True, blank=True, upload_to=photo_directory_path)
    phone = models.PositiveBigIntegerField(default=0, null=True, blank=True, help_text="Формат: 83517772233", verbose_name='Телефон')
    address = models.CharField(max_length=150, verbose_name='Адрес проживания')
    date_birth = models.CharField(max_length=10, db_index=True, help_text="Формат: dd.mm.yyyy", verbose_name='Дата рождения')
    data_employment = models.CharField(max_length=10, db_index=True, help_text="Формат: dd.mm.yyyy", verbose_name='Дата трудоустройства')
    organization = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    category = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name='Разряд')
    electrical_safety_qualification = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='Разряд по электробезопасности')
    size_shoe = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='Размер обуви')
    size_clothing = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name='Размер одежды')
    size_hat = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='Размер головного убора')
    briefings = models.ManyToManyField(Briefing, blank=True, related_name="briefings", verbose_name='Инструктажи')
    passport = models.ForeignKey(Passport, on_delete=models.PROTECT, verbose_name='Паспорт')
    security_license = models.ForeignKey(Security_license, blank=True, on_delete=models.PROTECT, verbose_name='Удостоверение частного охранника')
    driving_license = models.ForeignKey(Driving_license, blank=True, on_delete=models.PROTECT, verbose_name='Водительское удостоверение')
    medical_certificate = models.ForeignKey(Medical_certificate, blank=True, on_delete=models.PROTECT, verbose_name='Медицинская справка')
    periodic_inspection = models.ForeignKey(Periodic_inspection, blank=True, on_delete=models.PROTECT, verbose_name='Периодическая проверка')
    electrical_certificate = models.ForeignKey(Electrical_certificate, blank=True, on_delete=models.PROTECT, verbose_name='Удостоверение по ЭБ')
    uniforms = models.ManyToManyField(Uniform, blank=True, related_name="uniforms", verbose_name='Униформа')
    archived = models.BooleanField(default=False, verbose_name='Уволен')

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.middle_name}"
