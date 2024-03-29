from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from .views import IndexView, MovimientoCalculoView, ServicioCostoView, GraficoView, GraficoFechaView, ServicioSeguroCosto,ReportemensualView, \
    ReportesegurosView, MovMensualView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='agenda-index')),
    path('movcalculo', login_required(MovimientoCalculoView.as_view()), name='ajaxmov_calculo'),
    path('servicio-costo', login_required(ServicioCostoView.as_view()), name="servicio_costo"),
    path('seguro-servicio-costo', login_required(ServicioSeguroCosto.as_view()), name="seguro-servicio_costo"),
    path('grafico', login_required(GraficoView.as_view()), name="grafico"),
    path('graficofecha/<year>', login_required(GraficoFechaView.as_view()), name="grafico_fecha"),
    path('reportemensual', login_required(ReportemensualView.as_view()), name="reporte-mensual"),
    path('reporteseguros', login_required(ReportesegurosView.as_view()), name="reporte-seguros"),
    path('movmensual', login_required(MovMensualView.as_view()), name='movmensual')
]