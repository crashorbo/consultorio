import uuid
from django.db import models

from seguro.models import Seguro

# Create your models here.
class IngresoParticular(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_deposito = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='reporte/particular/', null=True, blank=True)
    estado = models.BooleanField(default=False)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


class IngresoSeguro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)    
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_deposito = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='reporte/seguro/', null=True, blank=True)
    estado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)