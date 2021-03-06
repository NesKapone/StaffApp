# Generated by Django 3.2.5 on 2021-07-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic_app', '0005_alter_userlocation_loc_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='loc_class',
            field=models.CharField(choices=[('badge rounded-pill bg-primary', 'синий'), ('badge rounded-pill bg-secondary', 'серый'), ('badge rounded-pill bg-success', 'зеленый'), ('badge rounded-pill bg-info text-dark', 'голубой'), ('badge rounded-pill bg-warning text-dark', 'желтый'), ('badge rounded-pill bg-danger', 'красный'), ('badge rounded-pill bg-light text-dark', 'светлый'), ('badge rounded-pill bg-dark', 'темный')], default='badge badge-pill badge-primary', max_length=200, verbose_name='Класс bootstrap'),
        ),
    ]
