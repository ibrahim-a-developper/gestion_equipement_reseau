# Generated by Django 3.0.8 on 2020-08-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0007_remove_equipement_equipement_installe'),
        ('installation', '0008_auto_20200805_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='equipement_installe',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='installation_equipement', to='equipement.Equipement'),
            preserve_default=False,
        ),
    ]
