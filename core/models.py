from enum import Enum

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class DefaultAbstractClass(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class UserRole(Enum):
    CUSTOMER = 'CUSTOMER_ROLE'
    COURIER = 'COURIER_ROLE'
    ADMIN = 'ADMINISTRATOR_ROLE'
    MANAGER = 'MANAGER_ROLE'

    @classmethod
    def as_choices(cls):
        return (
            (cls.CUSTOMER.value, 'Покупатель'),
            (cls.COURIER.value, 'Курьер'),
            (cls.ADMIN.value, 'Администратор'),
            (cls.MANAGER.value, 'Менеджер'),
        )


class User(AbstractUser):
    middle_name = models.CharField(max_length=200, blank=True, verbose_name='Отчество')
    name = models.CharField(max_length=200, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, blank=True, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='Email', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=100, choices=UserRole.as_choices(), default=UserRole.CUSTOMER.value,
                            verbose_name='Принадлежность')

    def __str__(self):
        return str(f"{self.name} {self.last_name}")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
