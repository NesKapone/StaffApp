# Generated by Django 3.2.5 on 2021-08-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic_app', '0013_alter_userstatistic_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_location',
        ),
    ]
