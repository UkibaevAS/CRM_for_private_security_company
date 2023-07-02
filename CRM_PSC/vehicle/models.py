from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import Affiliated_company
from document.models import Document
from equipment.models import Radio_station, Video_recorder, Armor
from worker.models import Worker


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
        ("without limitation", "without limitation"),
        ("limited", "limited"),
    ]

    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    branding = models.BooleanField(default=False)
    VIN_number = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                  verbose_name=_('VIN_number'))
    license_plate = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                     verbose_name=_('license_plate'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    date_purchase = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"),
                                     verbose_name=_('date_purchase'))
    registration_certificate = models.ManyToManyField(Document, related_name="registration_certificate",
                                                      verbose_name=_('registration_certificate'))
    passport_copy = models.ManyToManyField(Document, related_name="passport_copy_vehicle",
                                           verbose_name=_('passport'))
    insurance_policy_limit = models.CharField(max_length=18, choices=INSURANCE_LIMIT_CHOISES,
                                              default='without limitation', db_index=True,
                                              verbose_name=_('policy_limit'))
    is_listed_insurance = models.ManyToManyField(Worker, related_name="is_listed_insurance",
                                                 verbose_name=_('is_listed_insurance'))
    date_expiration_insurance = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                                 help_text=_("format data: dd.mm.yyyy"),
                                                 verbose_name=_('date_expiration_insurance'))
    insurance_policy_copy = models.ManyToManyField(Document, related_name="insurance_policy_copy",
                                                   verbose_name=_('insurance_policy'))
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('mileage'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('service_date'))
    engine_oil = models.CharField(max_length=20, null=True, blank=True, db_index=True,
                                  verbose_name=_('engine_oil'))
    engine_oil_viscosity = models.CharField(max_length=6, choices=ENGINE_OIL_VISCOSITY_GRADE_CHOICES, default='5W-40',
                                            db_index=True, verbose_name=_('oil_viscosity'))
    radio_stations = models.ManyToManyField(Radio_station, related_name="radio_stations_vehicle",
                                            verbose_name=_('radio_stations'))
    video_recorders = models.ManyToManyField(Video_recorder, related_name="video_recorders_vehicle",
                                             verbose_name=_('video_recorders'))
    armors = models.ManyToManyField(Armor, related_name="armors_vehicle", verbose_name=_('armors'))
