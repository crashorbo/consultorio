# Generated by Django 2.1.4 on 2019-01-28 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20190128_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 1, 28, 14, 30, 39, 556400)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2019, 1, 28, 14, 30, 39, 556370)),
        ),
    ]
