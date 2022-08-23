# Generated by Django 4.1 on 2022-08-23 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(help_text='Обязательное. Максимум - 100 символов.', max_length=150, verbose_name='Название ресторана')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Адрес ресторана')),
                ('logo', models.ImageField(upload_to='restaurant/logo/', verbose_name='Логотип')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
    ]
