# Generated by Django 2.2.8 on 2020-09-30 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0020_auto_20200917_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 9, 30, 4, 10, 42, 564227)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2020, 9, 30, 4, 10, 42, 564227)),
        ),
    ]
