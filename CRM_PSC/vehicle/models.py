from django.db import models
from django.utils.translation import gettext_lazy as _

from document.models import Document
from equipment.models import Radio_station, Video_recorder, Armor
from worker.models import Worker


def reg_certificate_number_copy_directory_path(instance: "Vehicle", filename: str) -> str:
    return "vehicle/certificate_number_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def insurance_policy_directory_path(instance: "Vehicle", filename: str) -> str:
    return "vehicle/insurance_policy_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Vehicle(models.Model):
    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name_vehicle'))
    branding = models.BooleanField(default=False)
    VIN_number = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                  verbose_name=_('VIN_number'))
    license_plate = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                     verbose_name=_('license_plate'))
    date_manufacture = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    date_purchase = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"),
                                     verbose_name=_('date_purchase'))
    registration_certificate_number = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                                       verbose_name=_('registration_certificate_number'))
    reg_certificate_number_copy = models.ImageField(null=True, blank=True,
                                                    upload_to=reg_certificate_number_copy_directory_path,
                                                    verbose_name=_('reg_certificate_number_copy'))
    passport_number = models.CharField(max_length=11, null=False, blank=False, db_index=True,
                                       help_text=_("format number: 1234 123456"),
                                       verbose_name=_('passport_number'))
    passport_copy = models.ManyToManyField(Document, related_name="passport_copy_vehicle",
                                           verbose_name=_('passport_vehicle'))
    number_insurance_policy = models.CharField(max_length=20, null=False, blank=False, db_index=True,
                                               verbose_name=_('number_insurance_policy'))
    date_expiration_insurance = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                                 help_text=_("format data: dd.mm.yyyy"),
                                                 verbose_name=_('date_expiration_insurance'))
    date_expiration_insurance = models.ImageField(null=True, blank=True, upload_to=insurance_policy_directory_path,
                                                  verbose_name=_('insurance_policy'))
    is_listed_insurance = models.ManyToManyField(Worker, related_name="is_listed_insurance",
                                                 verbose_name=_('is_listed_insurance'))
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('mileage'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date_vehicle'))
    engine_oil = models.CharField(max_length=20, null=True, blank=True, db_index=True,
                                  verbose_name=_('engine_oil'))
    radio_stations = models.ManyToManyField(Radio_station, related_name="radio_stations_vehicle", verbose_name=_('radio_stations'))
    video_recorders = models.ManyToManyField(Video_recorder, related_name="video_recorders_vehicle", verbose_name=_('video_recorders'))
    armors = models.ManyToManyField(Armor, related_name="armors_vehicle", verbose_name=_('armors'))