# Generated by Django 3.0.8 on 2020-09-13 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0016_auto_20200913_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='date_installe',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
