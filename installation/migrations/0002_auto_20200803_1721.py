# Generated by Django 3.0.8 on 2020-08-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='ville',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='direction',
            name='lieu',
            field=models.CharField(max_length=10),
        ),
    ]
