# Generated by Django 2.1.4 on 2018-12-18 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(default=django.utils.timezone.now)),
                ('documento', models.IntegerField(choices=[(1, 'CEDULA DE IDENTIDAD'), (2, 'PASAPORTE'), (3, 'CERTIFICADO DE NACIMIENTO')], default=1)),
                ('nro_documento', models.CharField(blank=True, max_length=20)),
                ('direccion', models.TextField(blank=True)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('ocupacion', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
