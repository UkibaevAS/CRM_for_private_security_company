from django.db import models


from config.models import Affiliated_company, Department, Position
from document.models import Passport, Driving_license, Security_license, Medical_certificate, Periodic_inspection, Electrical_certificate, Briefing
# from equipment.models import Uniform




def photo_directory_path(instance: "Worker", filename: str) -> str:
    return "Worker/photo/{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Worker(models.Model):
    CATEGORY_CHOISES = [
        ("Нет разряда", "Нет разряда"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]

    ELECTRICAL_QUALIFICATION_CHOISES = [
        ("Нет разряда", "Нет разряда"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    second_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    photo = models.ImageField(null=True, blank=True, upload_to=photo_directory_path)
    phone = models.PositiveBigIntegerField(default=8, null=True, blank=True, help_text="Формат: 83517772233", verbose_name='Телефон')
    address = models.CharField(max_length=150, verbose_name='Адрес проживания')
    date_birth = models.DateField(verbose_name='Дата рождения')
    official_employment = archived = models.BooleanField(default=False, verbose_name='Официальное трудоустройство')
    data_employment = models.DateField(verbose_name='Дата трудоустройства')
    organization = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT, related_name="organization")
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    category = models.CharField(max_length=11, choices=CATEGORY_CHOISES, default='Нет разряда', db_index=True, verbose_name='Разряд')
    electrical_safety_qualification = models.CharField(max_length=11, choices=ELECTRICAL_QUALIFICATION_CHOISES, default='Нет разряда', verbose_name='Разряд по электробезопасности')
    briefings = models.ManyToManyField(Briefing, blank=True, related_name="briefings", verbose_name='Инструктажи')
    passport = models.ForeignKey(Passport, on_delete=models.PROTECT, verbose_name='Паспорт')
    security_license = models.ForeignKey(Security_license, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Удостоверение частного охранника')
    driving_license = models.ForeignKey(Driving_license, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Водительское удостоверение')
    medical_certificate = models.ForeignKey(Medical_certificate, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Медицинская справка')
    periodic_inspection = models.ForeignKey(Periodic_inspection, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Периодическая проверка')
    electrical_certificate = models.ForeignKey(Electrical_certificate, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Удостоверение по ЭБ')
    # uniforms = models.ManyToManyField(Uniform, null=True, blank=True, related_name="uniforms", verbose_name='Униформа')
    archived = models.BooleanField(default=False, verbose_name='Уволен')

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.middle_name}"