from enum import Enum

from django.db import models
from core.models import DefaultAbstractClass, User


class DriverTransport(Enum):
    CAR = 'CAR'
    SCOOTER = 'SCOOTER'
    BICYCLE = 'BICYCLE'
    BOAT = 'BOAT'
    HELICOPTER = 'HELICOPTER'
    WALK = 'WALK'

    @classmethod
    def as_choice(cls):
        return (
            (cls.CAR.value, 'Машина'),
            (cls.SCOOTER.value, 'Скутер'),
            (cls.BICYCLE.value, 'Велосипед'),
            (cls.HELICOPTER.value, 'Вертолет?'),
            (cls.BOAT.value, 'Лодка?'),
            (cls.WALK.value, 'Пешком'),
        )


class CustomerProfile(DefaultAbstractClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile',
                                verbose_name='Профиль клиента')
    avatar = models.ImageField('Фото', upload_to='customer/avatars/', blank=True)
    address = models.CharField('Адрес', max_length=200, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class DriverProfile(DefaultAbstractClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile',
                                verbose_name='Профиль курьера')
    avatar = models.ImageField('Фото', upload_to='driver/avatars/', blank=True)
    transport = models.CharField('Вид транспорта', choices=DriverTransport.as_choice(),
                                 default=DriverTransport.WALK.value, max_length=50, help_text='Обязательное поле')
    plate_number = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        self.user.get_full_name()
