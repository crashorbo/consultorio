# Generated by Django 3.1.1 on 2020-09-17 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0019_auto_20200916_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 9, 17, 2, 17, 56, 404624)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2020, 9, 17, 2, 17, 56, 404612)),
        ),
    ]
