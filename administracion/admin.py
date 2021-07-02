from django.contrib import admin
from .models import IngresoParticular, IngresoSeguro
# Register your models here.
admin.site.register(IngresoSeguro)
admin.site.register(IngresoParticular)
