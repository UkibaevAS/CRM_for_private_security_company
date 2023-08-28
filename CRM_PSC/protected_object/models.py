from django.db import models


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
                                       verbose_name='Режим охраны')
    start_day_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                       help_text="Начало в: 08.00",
                                       verbose_name='Начало дневной смены в будни')
    start_day_shift_free_day = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                                help_text="Начало в: 08.00",
                                                verbose_name='Начало дневной смены в выходные')
    end_day_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                                help_text="Окончание в: 17.00",
                                                verbose_name='Окончание дневной смены в выходные')
    start_night_shift = models.CharField(max_length=5, null=True, blank=True, db_index=True,
                                         help_text="Начало в: 20.00",
                                         verbose_name='Начало ночной смены')
    phone = models.PositiveBigIntegerField(default=8, null=True, blank=True, db_index=True,
                                           help_text="Формат: 83517772233", verbose_name='Телефон')
    number_24 = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                      help_text="Количество охранников при круглосуточной охране",
                                                      verbose_name='Количество охранников круглосуточно')
    number_per_day = models.PositiveSmallIntegerField(default=0, null=True, blank=True, help_text="Количество охранников в дневную смену",
                                                        verbose_name='Количество охранников в дневную смену')
    number_per_night = models.PositiveSmallIntegerField(default=0, null=True, blank=True, help_text="Количество охранников в ночную смену",
                                                        verbose_name='Количество охранников в ночную смену')


    def __str__(self):
        return f"{self.name}"

class Protected_object(models.Model):
    class Meta:
        verbose_name = 'Охраняемый объект'
        verbose_name_plural = 'Охраняемые объекы'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название объекта')
    address = models.CharField(max_length=100, db_index=True, verbose_name='Адрес')
    curator = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Куратор')
    posts = models.ManyToManyField(Post, blank=True, related_name="posts", verbose_name='Посты')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Заказчик')
    performer = models.ForeignKey(Performer, on_delete=models.PROTECT, verbose_name='Кто реагирует на сработки')
    armors = models.ManyToManyField(Armor, blank=True, related_name="armors_post", verbose_name='Средства бронезащиты')
    guns = models.ManyToManyField(Gun, blank=True, related_name="guns_post", verbose_name='Вооружение')
    radio_station = models.ManyToManyField(Radio_station, blank=True, related_name="radio_stations_post",
                                           verbose_name='Радиостанция')
    webcams = models.ManyToManyField(Webcam, blank=True, related_name="webcams_post", verbose_name='Видеокамеры')
    security_systems = models.ManyToManyField(Security_system, blank=True, related_name="security_systems",
                                              verbose_name='Охранные системы')
    alarm_systems = models.ManyToManyField(Alarm_system, blank=True, related_name="alarm_systems_post",
                                           verbose_name='Средства сигнализации')
    vehicle = models.ManyToManyField(Vehicle, blank=True, related_name="vehicles_post", verbose_name='Автомобиль')
    foto = models.FileField(null=True, blank=True, upload_to=copy_directory_path, verbose_name='Фото объекта')

    def __str__(self):
        return f"{self.name}"
