from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import Affiliated_company


class Uniform(models.Model):
    class Meta:
        verbose_name = _('Uniform')
        verbose_name_plural = _('Uniforms')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name_uniform'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description_uniform'))
    size = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('size_uniform'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)

    def __str__(self):
        return f"{_('Uniform')}(pk={self.pk}, name={self.name!r})"


class Gun(models.Model):
    class Meta:
        verbose_name = _('Gun')
        verbose_name_plural = _('Guns')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_manufacture'))
    date_test_shoot = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_test_shoot'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))


class Handcuffs(models.Model):
    class Meta:
        verbose_name = _('Handcuffs')
        verbose_name_plural = _('Handcuffs')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=True, blank=True, db_index=True,
                                      verbose_name=_('factory_number'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))


class Rubber_stick(models.Model):
    class Meta:
        verbose_name = _('Rubber_stick')
        verbose_name_plural = _('Rubber_sticks')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"), verbose_name=_('receipt_date'))


class Special_spray(models.Model):
    class Meta:
        verbose_name = _('Special_spray')
        verbose_name_plural = _('Special_sprays')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    expiration_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"),
                                       verbose_name=_('expiration_date'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date'))


class Armor(models.Model):
    class Meta:
        verbose_name = _('Armor')
        verbose_name_plural = _('Armors')

    name = models.CharField(max_length=15, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=150, null=True, blank=True, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=True, blank=True, db_index=True,
                                      verbose_name=_('factory_number'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    protection_category = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True,
                                                   verbose_name=_('protection_category'))
    date_purchase = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                     help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_purchase'))


class Video_recorder(models.Model):
    class Meta:
        verbose_name = _('Video_recorder')
        verbose_name_plural = _('Video_recorders')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date'))
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                            help_text=_("number of months: XX"),
                                            verbose_name=_('maintenance_interval'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next'))


class Radio_station(models.Model):
    class Meta:
        verbose_name = _('Radio_station')
        verbose_name_plural = _('Radio_stations')

    name = models.CharField(max_length=20, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True,
                                   verbose_name=_('description'))
    factory_number = models.CharField(max_length=15, null=False, blank=False, db_index=True,
                                      verbose_name=_('factory_number'))
    owner = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('installation_date'))
    maintenance_interval = models.CharField(max_length=15, null=True, blank=True, db_index=True,
                                            help_text=_("number of months: XX"),
                                            verbose_name=_('maintenance_interval'))
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text=_("format data: dd.mm.yyyy"),
                                        verbose_name=_('date_manufacture'))
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('receipt_date'))
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text=_("format data: dd.mm.yyyy"),
                                    verbose_name=_('service_date'))
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text=_("format data: dd.mm.yyyy"),
                                         verbose_name=_('service_date_next'))
