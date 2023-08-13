from django.db import models
# from django.utils.translation import gettext_lazy as _

from config.models import Affiliated_company
from document.models import Registration_certificate, Vehicle_passport, Insurance_policy
from equipment.models import Radio_station, Video_recorder, Armor


class Vehicle(models.Model):
    ENGINE_OIL_VISCOSITY_GRADE_CHOICES = [
        ("0W-20", "0W-20"),
        ("0W-30", "0W-30"),
        ("0W-40", "0W-40"),
        ("5W-20", "5W-20"),
        ("5W-30", "5W-30"),
        ("5W-40", "5W-40"),
        ("10W-20", "10W-20"),
        ("10W-30", "10W-30"),
        ("10W-40", "10W-40"),
        ("15W-30", "15W-30"),
        ("15W-40", "15W-40"),
        ("20W-30", "20W-30"),
        ("20W-40", "20W-40"),
    ]

    INSURANCE_LIMIT_CHOISES = [
        ("Без ограничения", "Без ограничения"),
        ("Ограниченная", "Ограниченная"),
    ]

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    name = models.CharField(max_length=20, verbose_name='Марка автомобиля')
    branding = models.BooleanField(default=False, verbose_name='Наличие брендовой оклейки')
    VIN_number = models.CharField(max_length=20, verbose_name='VIN номер')
    license_plate = models.CharField(max_length=20, verbose_name='Номерной знак')
    owner_company = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Владелец ТС юрлицо')
    owner_private = models.CharField(max_length=20, null=True, blank=True, verbose_name='Владелец ТС частное лицо', help_text="Фамилия и инициалы")
    date_manufacture = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата производства')
    receipt_date = models.DateField(null=True, blank=True, verbose_name='Дата поступления')
    registration_certificate = models.ManyToManyField(Registration_certificate, related_name="registration_certificate",
                                                      verbose_name='Свидетельство о регистрации ТС')
    passport_copy = models.ManyToManyField(Vehicle_passport, related_name="passport_copy_vehicle",
                                           verbose_name='Паспорт транспортного средства')
    insurance_policy_limit = models.CharField(max_length=18, choices=INSURANCE_LIMIT_CHOISES,
                                              default='Без ограничения', verbose_name='Вид страховки')
    insurance_policy_copy = models.ManyToManyField(Insurance_policy, related_name="insurance_policy_copy",
                                                   verbose_name='Страховой полис')
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Пробег, км')
    service_date = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата проведенного ТО')
    engine_oil = models.CharField(max_length=20, null=True, blank=True, verbose_name='Марка моторного масла')
    engine_oil_viscosity = models.CharField(max_length=6, choices=ENGINE_OIL_VISCOSITY_GRADE_CHOICES, default='5W-40',
                                            verbose_name='Вязкость масла')
    radio_stations = models.ManyToManyField(Radio_station, related_name="radio_stations_vehicle", null=True, blank=True,
                                            verbose_name='Радиостанция')
    video_recorders = models.ManyToManyField(Video_recorder, related_name="video_recorders_vehicle", null=True,
                                             blank=True,
                                             verbose_name='Видеорегистратор')
    armors = models.ManyToManyField(Armor, related_name="armors_vehicle", null=True, blank=True,
                                    verbose_name='Бронезащита')

    def __str__(self):
        return f"{self.license_plate}"