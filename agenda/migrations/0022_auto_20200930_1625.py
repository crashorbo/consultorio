# Generated by Django 2.2.8 on 2020-09-30 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0021_auto_20200930_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 9, 30, 16, 25, 16, 141831)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2020, 9, 30, 16, 25, 16, 141831)),
        ),
    ]
