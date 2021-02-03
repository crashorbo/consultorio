from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .reporte import reporte_seguro, reporte_particular
from .models import IngresoParticular, IngresoSeguro
from .forms import IngresosParticularForm, IngresosParticularDepositoForm, IngresosSeguroForm, IngresosSeguroDepositoForm
from agenda.models import Agendaserv, Seguro
# Create your views here.

def ingresos_particular(request):
    ingresos_list = IngresoParticular.objects.all().order_by('-fecha_inicio')
    page = request.GET.get('page', 1)
    paginator = Paginator(ingresos_list, 12)
    try:
        ingresos = paginator.page(page)
    except PageNotAnInteger:
        ingresos = paginator.page(1)
    except EmptyPage:
        ingresos = paginator.page(paginator.num_pages)        
    return render(request, 'administracion/ingresos-particular.html', {'ingresos': ingresos})

def ingresos_particular_filtro(request):
    ingresos_list = IngresoParticular.objects.filter(fecha_inicio__range=(request.GET.get('fechaini'), request.GET.get('fechafin')))
    suma = ingresos_list.aggregate(Sum('total'))['total__sum'] or 0.00    
    return render(request, 'administracion/ingresos-particular-list.html', {'ingresos': ingresos_list, 'total': suma})

def ingresos_particular_deposito(request, pk):
    ingreso = IngresoParticular.objects.get(id=pk)
    form = IngresosParticularDepositoForm(instance=ingreso)
    if request.method == 'POST':
        form = IngresosParticularDepositoForm(request.POST, request.FILES, instance=ingreso)
        if form.is_valid():
            ingreso = form.save()
        return JsonResponse({"message": "Se ha registrado con exito el Ingreso", "state":"success"}, status=200)  
    return render(request, 'administracion/ingresos-particular-deposito.html', {'form': form, 'ingreso': ingreso})

def ingresos_particular_create(request):
    form = IngresosParticularForm()
    if request.method == 'POST':
        form = IngresosParticularForm(request.POST)        
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.total = Agendaserv.objects.filter(agenda__tipo=0, fecha__range=(ingreso.fecha_inicio, ingreso.fecha_fin), agenda__deleted=False).aggregate(Sum('costo'))['costo__sum'] or 0.00
            ingreso.ingreso = ingreso.total
            ingreso.save()
            return JsonResponse({"message": "Se ha registrado con exito el Ingreso", "state":"success"}, status=200)  
    return render(request, 'administracion/ingresos-particular-create.html', {'form': form})

def ingresos_seguro(request):
    seguros = Seguro.objects.all().order_by('nombre')    
    ingresos_list = IngresoSeguro.objects.all().order_by('-fecha_inicio')    
    page = request.GET.get('page', 1)
    paginator = Paginator(ingresos_list, 12)
    try:
        ingresos = paginator.page(page)
    except PageNotAnInteger:
        ingresos = paginator.page(1)
    except EmptyPage:
        ingresos = paginator.page(paginator.num_pages)
    return render(request, 'administracion/ingresos-seguro.html', {'seguros': seguros, 'ingresos': ingresos})

def ingresos_seguro_filtro(request):
    ingresos_list = IngresoSeguro.objects.filter(fecha_inicio__range=(request.GET.get('fechaini'), request.GET.get('fechafin')), seguro=request.GET.get('seguroini'))
    suma = ingresos_list.aggregate(Sum('total'))['total__sum'] or 0.00
    print(suma) 
    return render(request, 'administracion/ingresos-seguro-list.html', {'ingresos': ingresos_list, 'total': suma})

def ingresos_seguro_create(request):
    form = IngresosSeguroForm()
    if request.method == 'POST':
        form = IngresosSeguroForm(request.POST)        
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.total = Agendaserv.objects.filter(agenda__seguro=ingreso.seguro, agenda__tipo=1, fecha__range=(ingreso.fecha_inicio, ingreso.fecha_fin), agenda__deleted=False).aggregate(Sum('costo'))['costo__sum'] or 0.00
            ingreso.save()
            return JsonResponse({"message": "Se ha registrado con exito el Ingreso", "state":"success"}, status=200)  
    return render(request, 'administracion/ingresos-seguro-create.html', {'form': form})

def ingresos_seguro_deposito(request, pk):
    ingreso = IngresoSeguro.objects.get(id=pk)
    form = IngresosSeguroDepositoForm(instance=ingreso)
    if request.method == 'POST':
        form = IngresosSeguroDepositoForm(request.POST, request.FILES, instance=ingreso)
        if form.is_valid():
            ingreso = form.save()
        return JsonResponse({"message": "Se ha registrado con exito el Ingreso", "state":"success"}, status=200)  
    return render(request, 'administracion/ingresos-seguro-deposito.html', {'form': form, 'ingreso': ingreso})

def ingresos_seguro_reporte(request, pk):
    ingreso = IngresoSeguro.objects.get(id=pk)
    ingresos = Agendaserv.objects.filter(agenda__seguro=ingreso.seguro, agenda__tipo=1, fecha__range=(ingreso.fecha_inicio, ingreso.fecha_fin), agenda__deleted=False).order_by('fecha')
    total = ingresos.aggregate(Sum('costo'))['costo__sum'] or 0.00    
    return reporte_seguro(ingreso, ingresos, total)

def ingresos_particular_reporte(request, pk):
    ingreso = IngresoParticular.objects.get(id=pk)
    ingresos = Agendaserv.objects.filter(agenda__tipo=0, fecha__range=(ingreso.fecha_inicio, ingreso.fecha_fin), agenda__deleted=False).order_by('fecha')
    total = ingresos.aggregate(Sum('costo'))['costo__sum'] or 0.00    
    return reporte_particular(ingreso, ingresos, total)