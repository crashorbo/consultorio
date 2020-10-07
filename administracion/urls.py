from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('ingresos-particular/', login_required(views.ingresos_particular), name='ingresos-particular'),
    path('ingresos-particular-create/', login_required(views.ingresos_particular_create), name='ingresos-particular-create'),
    path('ingresos-particular-deposito/<pk>/', login_required(views.ingresos_particular_deposito), name='ingresos-particular-deposito'),
    path('ingresos-particular-filtro/', login_required(views.ingresos_particular_filtro), name='ingresos-particular-filtro'),
    path('ingresos-seguro/', login_required(views.ingresos_seguro), name='ingresos-seguro'),
    path('ingresos-seguro-create/', login_required(views.ingresos_seguro_create), name='ingresos-seguro-create'),
    path('ingresos-seguro-deposito/<pk>/', login_required(views.ingresos_seguro_deposito), name='ingresos-seguro-deposito'),
    path('ingresos-seguro-filtro/', login_required(views.ingresos_seguro_filtro), name='ingresos-seguro-filtro'),
    path('ingresos-seguro-reporte/<pk>/', login_required(views.ingresos_seguro_reporte), name='ingresos-seguro-reporte'),
]