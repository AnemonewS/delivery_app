from django.db import models
from core.models import DefaultAbstractClass, User


class Restaurant(DefaultAbstractClass):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='restaurant', verbose_name='Владелец')
    title = models.CharField('Название ресторана', max_length=150, help_text='Обязательное. Максимум - 100 символов.')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    address = models.CharField('Адрес ресторана', max_length=150, blank=True)
    logo = models.ImageField('Логотип', upload_to='restaurant/logo/')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
