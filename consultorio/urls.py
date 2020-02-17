"""consultorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('agenda/', include('agenda.urls')),
    path('paciente/', include('paciente.urls')),
    path('seguro/', include('seguro.urls')),
    path('servicio/', include('servicio.urls')),
    path('medicamento/', include('medicamento.urls')),
    path('configuracion/', include('configuracion.urls')),
    path('reporte/', include('reporte.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
