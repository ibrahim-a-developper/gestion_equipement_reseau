# Generated by Django 3.0.8 on 2020-08-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0003_auto_20200728_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nom'),
        ),
    ]