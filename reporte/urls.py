from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.reporte_index), name='reporte-index'),
    path('particulares/', login_required(views.reporte_particulares_index), name='reporte-particulares'),
    path('seguros/', login_required(views.reporte_seguros_index), name='reporte-seguros')
]
