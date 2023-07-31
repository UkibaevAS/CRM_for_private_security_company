from django.db import models
from django.utils.translation import gettext_lazy as _


class Affiliated_company(models.Model):
    class Meta:
        verbose_name = 'Аффилированная (дочерняя) компания'
        verbose_name_plural = 'Аффилированные (дочернии) компании'

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))
    address = models.CharField(max_length=100, db_index=True, verbose_name=_('address'))
    phone = models.PositiveBigIntegerField(default=0, null=True, blank=True, db_index=True,
                                           help_text=_("format phone: 83517772233"), verbose_name=_('phone'))
    email = models.EmailField(max_length=254)
    INN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name=_('INN'))
    OGRN = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name=_('OGRN'))
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('bank_details'))
    director = models.CharField(max_length=75, db_index=True, verbose_name=_('director'))
    contact_person = models.CharField(max_length=75, db_index=True, verbose_name=_('contact_person'))
    phone_contact_person = models.PositiveBigIntegerField(default=0, null=True, blank=True,
                                                          db_index=True, help_text=_("format phone: 83517772233"),
                                                          verbose_name=_('phone_contact_person'))

    def __str__(self):
        return f"{self.name!r}"
class Department(models.Model):
    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))
    manager = models.CharField(max_length=75, db_index=True, verbose_name=_('manager'))

    def __str__(self):
        return f"{self.name!r}"


class Position(models.Model):
    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))

    def __str__(self):
        return f"{self.name!r}"