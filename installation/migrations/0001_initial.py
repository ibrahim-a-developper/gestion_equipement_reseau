# Generated by Django 3.0.8 on 2020-07-27 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('mac', models.CharField(max_length=50)),
                ('date_installe', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomD', to='installation.Direction')),
            ],
        ),
    ]
