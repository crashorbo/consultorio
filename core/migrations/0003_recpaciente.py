# Generated by Django 2.1.4 on 2019-04-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190422_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recpaciente',
            fields=[
                ('codigo', models.TextField(primary_key=True, serialize=False)),
                ('nombres', models.TextField(blank=True, null=True)),
                ('a_paterno', models.TextField(blank=True, null=True)),
                ('a_materno', models.TextField(blank=True, null=True)),
                ('de', models.TextField(blank=True, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('telefono', models.TextField(blank=True, null=True)),
                ('ocupacion', models.TextField(blank=True, null=True)),
                ('ci', models.TextField(blank=True, null=True)),
                ('fecha_reg', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rec_paciente',
                'managed': False,
            },
        ),
    ]