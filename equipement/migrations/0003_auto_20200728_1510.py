# Generated by Django 3.0.8 on 2020-07-28 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0001_initial'),
        ('equipement', '0002_auto_20200727_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='equipement_installe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installation.Installation'),
        ),
    ]
