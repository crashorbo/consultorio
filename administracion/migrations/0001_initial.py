# Generated by Django 2.2.8 on 2020-09-30 20:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seguro', '0002_segurocosto'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresoParticular',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_deposito', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reporte/particular/')),
                ('estado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoSeguro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_deposito', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reporte/seguro/')),
                ('estado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('seguro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguro.Seguro')),
            ],
        ),
    ]