# Generated by Django 2.1.4 on 2019-07-24 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0012_auto_20190722_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 7, 23, 22, 18, 50, 557674)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2019, 7, 23, 22, 18, 50, 557652)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='procedencia',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]