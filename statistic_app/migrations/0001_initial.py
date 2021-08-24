# Generated by Django 3.2.5 on 2021-07-21 13:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
                ('tabel_num', models.IntegerField(default=0, verbose_name='Табельный номер')),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('url', models.SlugField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание события')),
                ('pub_date', models.DateField(default=django.utils.timezone.now, verbose_name='Время изменения')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True, verbose_name='Местоположение пользователя')),
                ('loc_description', models.TextField(blank=True, null=True, verbose_name='Описание местоположение')),
                ('loc_class', models.CharField(max_length=200, verbose_name='Класс bootstrap')),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='UserStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание события')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 7, 21, 16, 0, 2, 196841), verbose_name='Время публикации')),
                ('user_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistic_app.userlocation', verbose_name='Местоположение пользователя')),
                ('user_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistic_app.profile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Статистика пользователя',
                'verbose_name_plural': 'Статистика пользователей',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistic_app.userlocation', verbose_name='Местоположение пользователя'),
        ),
    ]