from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ExamenCreateView, ExamenListView, IndexView, AjaxListView, TableAsJSON, AjaxCrearView, AjaxEditarView, AjaxEliminarView

urlpatterns = [
  path('', login_required(IndexView.as_view()), name='configuracion'),
  url(r'^as_json/$',login_required(TableAsJSON.as_view()), name='table-as-json'),
  path('tipo-lente/ajax-lista/', login_required(AjaxListView.as_view()), name='tipolente-ajax-lista'),
  path('tipo-lente/ajax-registrar/', login_required(AjaxCrearView.as_view()), name='tipolente-ajax-registrar'),
  path('tipo-lente/ajax-editar/<pk>', login_required(AjaxEditarView.as_view()), name='tipolente-ajax-editar'),
  path('tipo-lente/ajax-eliminar', login_required(AjaxEliminarView.as_view()), name='tipolente-ajax-eliminar'),
  path('examen/ajax/list/', login_required(ExamenListView.as_view()), name='examen-list'),
  path('examen/ajax/create/', login_required(ExamenCreateView.as_view()), name='examen-create'),
]
