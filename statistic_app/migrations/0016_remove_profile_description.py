# Generated by Django 3.2.5 on 2021-08-24 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic_app', '0015_profile_user_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
    ]