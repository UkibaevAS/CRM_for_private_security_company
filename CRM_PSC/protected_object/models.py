from django.db import models
from django.utils.translation import gettext_lazy as _

from equipment.models import Radio_station, Armor, Gun
from security_system.models import Webcam, Alarm_system, Security_system
from vehicle.models import Vehicle
from worker.models import Worker


def protected_object_foto_directory_path(instance: "Protected_object", filename: str) -> str:
    return "Protected_object/object_foto_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def security_contracts_directory_path(instance: "Protected_object", filename: str) -> str:
    return "Protected_object/security_contracts_object_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Post(models.Model):
    PROTECT_MODE_POST_CHOICES = [
        ("round-the-clock", "24/7"),
        ('daytime', _("Daytime")),
        ("nightly", _("Nightly")),
        ("mixed", _("Mixed")),
        ]

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name'))
    protection_mode = models.CharField(max_length=15, choices=PROTECT_MODE_POST_CHOICES, default='24/7', db_index=True,
                                       verbose_name=_('protection_mode'))  # список(круглосуточно, дневной, ночной)
    start_day_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"),
                                       verbose_name=_('start_day_shift'))
    start_day_shift_free_day = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"),
                                       verbose_name=_('start_day_shift_free_day'))
    start_night_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('start_night_shift'))
    phone = models.PositiveBigIntegerField(default=0, null=True, blank=True, db_index=True,
                                           help_text=_("format phone: 83517772233"), verbose_name=_('phone'))
    number_per_day = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                      verbose_name=_('number_per_day'))
    number_per_night = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                        verbose_name=_('number_per_night'))
    armors = models.ManyToManyField(Armor, related_name="armors_post", verbose_name=_('armors'))
    guns = models.ManyToManyField(Gun, related_name="guns_post", verbose_name=_('guns'))
    radio_stations = models.ManyToManyField(Radio_station, related_name="radio_stations_post",
                                            verbose_name=_('radio_stations'))
    webcams = models.ManyToManyField(Webcam, related_name="webcams_post", verbose_name=_('webcams'))
    alarm_systems = models.ManyToManyField(Alarm_system, related_name="alarm_systems_post",
                                           verbose_name=_('alarm_systems'))
    vehicles = models.ManyToManyField(Vehicle, related_name="vehicles_post", verbose_name=_('vehicles'))


class Client(models.Model):
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))
    address = models.CharField(max_length=100, db_index=True, verbose_name=_('address'))
    phone = models.PositiveBigIntegerField(default=0, null=True, blank=True, db_index=True,
                                           help_text=_("format phone: 83517772233"), verbose_name=_('phone'))
    email = models.EmailField(max_length=254)
    INN = models.PositiveBigIntegerField(default=0, null=False, blank=False, db_index=True,
                                         verbose_name=_('INN'))
    OGRN = models.PositiveBigIntegerField(default=0, null=False, blank=False, db_index=True,
                                          verbose_name=_('OGRN'))
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('bank_details'))
    director = models.CharField(max_length=75, db_index=True, verbose_name=_('director'))
    contact_person = models.CharField(max_length=75, db_index=True, verbose_name=_('contact_person'))
    phone_contact_person = models.PositiveBigIntegerField(default=0, null=True, blank=True,
                                                          db_index=True, help_text=_("format phone: 83517772233"),
                                                          verbose_name=_('phone_contact_person'))
    security_contracts = models.ImageField(null=True, blank=True, upload_to=security_contracts_directory_path,
                                           verbose_name=_('security_contracts'))


class Protected_object(models.Model):
    class Meta:
        verbose_name = _('Protected_object')
        verbose_name_plural = _('Protected_objects')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))
    address = models.CharField(max_length=100, db_index=True, verbose_name=_('address'))
    curator = models.ForeignKey(Worker, on_delete=models.PROTECT)
    security_method = models.CharField(max_length=50, db_index=True,
                                       verbose_name=_('security_method'))  # выбор из списка
    posts = models.ManyToManyField(Post, related_name="posts", verbose_name=_('posts'))
    foto = models.ImageField(null=True, blank=True, upload_to=protected_object_foto_directory_path,
                             verbose_name=_('foto'))
    security_systems = models.ManyToManyField(Security_system, related_name="security_systems",
                                              verbose_name=_('security_systems'))
    clients = models.ManyToManyField(Client, related_name="organizations", verbose_name=_('organizations'))
