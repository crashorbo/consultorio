# Generated by Django 2.2.8 on 2021-03-30 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0028_auto_20210315_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 3, 30, 8, 56, 28, 650511)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2021, 3, 30, 8, 56, 28, 650511)),
        ),
    ]
