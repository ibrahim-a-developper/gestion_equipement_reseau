# Generated by Django 3.0.8 on 2020-08-05 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0005_auto_20200805_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installation',
            name='date_update',
        ),
    ]