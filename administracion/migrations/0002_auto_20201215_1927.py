# Generated by Django 2.2.8 on 2020-12-15 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresoparticular',
            name='egreso',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='ingresoparticular',
            name='ingreso',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]