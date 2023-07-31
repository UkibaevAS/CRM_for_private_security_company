from django.db import models

from config.models import Affiliated_company


class Uniform(models.Model):
    class Meta:
        verbose_name = 'Униформа'
        verbose_name_plural = 'Униформа'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    size = models.SmallIntegerField(default=0, db_index=True, verbose_name='Размер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')

    def __str__(self):
        return f"{self.name}, 'size' - {self.size}"
        # return f"{_('Uniform')}(pk={self.pk}, name={self.name!r})"


class Gun(models.Model):
    class Meta:
        verbose_name = 'Вооружение'
        verbose_name_plural = 'Вооружение'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    date_test_shoot = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                       help_text="Формат: dd.mm.yyyy", verbose_name='Дата контрольного отстрела')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')


class Handcuffs(models.Model):
    class Meta:
        verbose_name = 'Наручники'
        verbose_name_plural = 'Наручники'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')


class Rubber_stick(models.Model):
    class Meta:
        verbose_name = 'Палка резиновая'
        verbose_name_plural = 'Палка резиновая'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')


class Special_spray(models.Model):
    class Meta:
        verbose_name = 'Аэрозоль специальный'
        verbose_name_plural = 'Аэрозоли специальные'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    expiration_date = models.CharField(max_length=10, db_index=True, help_text="Формат: dd.mm.yyyy",
                                       verbose_name='Срок годности')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')


class Armor(models.Model):
    class Meta:
        verbose_name = 'Бронезащита'
        verbose_name_plural = 'Бронезащита'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    protection_category = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='Класс защиты')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')


class Video_recorder(models.Model):
    class Meta:
        verbose_name = 'Видеорегистратор'
        verbose_name_plural = 'Видеорегистраторы'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text="Формат: dd.mm.yyyy", verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True, help_text="Количество месяцев: XX",
                                            verbose_name='Периодичность ТО')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата проведенного ТО')
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text="Формат: dd.mm.yyyy", verbose_name='Дата следующего ТО')


class Radio_station(models.Model):
    class Meta:
        verbose_name = 'Радиостанция'
        verbose_name_plural = 'Радиостанции'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    factory_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заводской номер')
    owner = models.ForeignKey(Affiliated_company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Числится на балансе')
    installation_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text="Формат: dd.mm.yyyy", verbose_name='Дата установки')
    maintenance_interval = models.CharField(max_length=15, null=False, blank=False, db_index=True, help_text="Количество месяцев: XX",
                                            verbose_name='Периодичность ТО')
    date_manufacture = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                        help_text="Формат: dd.mm.yyyy", verbose_name='Дата производства')
    receipt_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата поступления')
    service_date = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                    help_text="Формат: dd.mm.yyyy", verbose_name='Дата проведенного ТО')
    service_date_next = models.CharField(max_length=10, null=True, blank=True, db_index=True,
                                         help_text="Формат: dd.mm.yyyy", verbose_name='Дата следующего ТО')
