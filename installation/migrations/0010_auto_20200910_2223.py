# Generated by Django 3.0.8 on 2020-09-10 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0009_auto_20200809_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='lieu',
            new_name='Nom',
        ),
        migrations.RenameField(
            model_name='installation',
            old_name='direction',
            new_name='Nom_direction',
        ),
        migrations.RemoveField(
            model_name='direction',
            name='ville',
        ),
    ]
