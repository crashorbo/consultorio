# Generated by Django 2.2.8 on 2020-02-09 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0016_auto_20191211_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 2, 9, 2, 24, 41, 230658)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2020, 2, 9, 2, 24, 41, 230658)),
        ),
    ]
