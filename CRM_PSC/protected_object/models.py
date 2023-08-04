from django.db import models
from django.utils.translation import gettext_lazy as _

from equipment.models import Radio_station, Armor, Gun
from security_system.models import Webcam, Alarm_system, Security_system
from vehicle.models import Vehicle
from worker.models import Worker
from typing import Union
def copy_directory_path(instance:  Union["Client", "Performer"], filename: str) -> str:
    if isinstance(instance, Client):
        document_title = "client"
    else:
        document_title = "performer"
    return f"{document_title}/" + instance.name + "/{filename}".format(
        filename=filename,
    )




class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural ='Клиенты'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название организации')
    address = models.CharField(max_length=100, db_index=True, verbose_name='Адрес')
    phone = models.PositiveBigIntegerField(default=8, help_text="Формат: 83517772233", verbose_name='Телефон')
    email = models.EmailField(max_length=254, null=True, blank=True)
    INN = models.PositiveBigIntegerField(default=0, verbose_name='ИНН')
    OGRN = models.PositiveBigIntegerField(default=0, verbose_name='ОГРН')
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name='Банковские реквизиты')
    director = models.CharField(max_length=75, verbose_name='Директор')
    contact_person = models.CharField(max_length=75, verbose_name='Контактное лицо')
    phone_contact_person = models.PositiveBigIntegerField(default=8, help_text="Формат: 83517772233",
                                                          verbose_name='Телефон контактного лица')
    contract = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Договор об оказании услуг')

    def __str__(self):
        return f"{self.name}"

class Performer(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название организации')
    address = models.CharField(max_length=100, db_index=True, verbose_name='Адрес')
    phone = models.PositiveBigIntegerField(default=8, help_text="Формат: 83517772233", verbose_name='Телефон')
    email = models.EmailField(max_length=254, null=True, blank=True)
    INN = models.PositiveBigIntegerField(default=0, verbose_name='ИНН')
    OGRN = models.PositiveBigIntegerField(default=0, verbose_name='ОГРН')
    bank_details = models.CharField(max_length=200, null=True, blank=True, verbose_name='Банковские реквизиты')
    director = models.CharField(max_length=75, verbose_name='Директор')
    contact_person = models.CharField(max_length=75, verbose_name='Контактное лицо')
    phone_contact_person = models.PositiveBigIntegerField(default=8, help_text="Формат: 83517772233",
                                                          verbose_name='Телефон контактного лица')

    def __str__(self):
        return f"{self.name}"



class Post(models.Model):
    PROTECT_MODE_POST_CHOICES = [
        ("round-the-clock", "24/7"),
        ('daytime', "Дневной"),
        ("nightly", "Ночной"),
        ("mixed", "Смешанный"),
    ]

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')
    protection_mode = models.CharField(max_length=15, choices=PROTECT_MODE_POST_CHOICES, default='24/7', db_index=True,
                                       verbose_name='Время выставления поста')
    start_day_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                       help_text="Формат: dd.mm.yyyy",
                                       verbose_name='Начало дневной смены в будни')
    start_day_shift_free_day = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                                help_text="Формат: dd.mm.yyyy",
                                                verbose_name='Начало дневной смены в выходные')
    start_night_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                         help_text="Формат: dd.mm.yyyy",
                                         verbose_name='Начало ночной смены')
    phone = models.PositiveBigIntegerField(default=8, null=True, blank=True, db_index=True,
                                           help_text="Формат: 83517772233", verbose_name='Телефон')
    number_24 = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                      help_text="Количество охранников при круглосуточной охране",
                                                      verbose_name='Количество охранников круглосуточно')
    number_per_day = models.PositiveSmallIntegerField(default=0, null=True, blank=True, help_text="Количество охранников",
                                                        verbose_name='Количество охранников в дневную смену')
    number_per_night = models.PositiveSmallIntegerField(default=0, null=True, blank=True, help_text="Количество охранников",
                                                        verbose_name='Количество охранников в ночную смену')
    performer = models.ForeignKey(Performer, verbose_name='Исполнитель', on_delete=models.PROTECT)
    armors = models.ManyToManyField(Armor, null=True, blank=True, related_name="armors_post", verbose_name='Средства бронезащиты')
    guns = models.ManyToManyField(Gun, null=True, blank=True, related_name="guns_post", verbose_name='Вооружение')
    radio_station = models.ManyToManyField(Radio_station, null=True, blank=True, related_name="radio_stations_post",
                                            verbose_name='Радиостанция')
    webcams = models.ManyToManyField(Webcam, null=True, blank=True, related_name="webcams_post", verbose_name='Видеокамеры')
    alarm_systems = models.ManyToManyField(Alarm_system, null=True, blank=True, related_name="alarm_systems_post",
                                           verbose_name='Средства сигнализации')
    vehicle = models.ManyToManyField(Vehicle, null=True, blank=True, related_name="vehicles_post", verbose_name='Автомобиль')

    def __str__(self):
        return f"{self.name}"

class Protected_object(models.Model):
    class Meta:
        verbose_name = 'Охраняемый объект'
        verbose_name_plural = 'Охраняемые объекы'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название объекта')
    address = models.CharField(max_length=100, db_index=True, verbose_name='Адрес')
    curator = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Куратор')
    posts = models.ManyToManyField(Post, null=True, blank=True, related_name="posts", verbose_name='Посты')
    security_systems = models.ManyToManyField(Security_system, null=True, blank=True, related_name="security_systems",
                                              verbose_name='Охранные системы')
    clients = models.ManyToManyField(Client, related_name="organizations", verbose_name='Заказчик')
    performer = models.ForeignKey(Performer, on_delete=models.PROTECT, verbose_name='Исполнитель')
    foto = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Фото объекта')

    def __str__(self):
        return f"{self.name}"
