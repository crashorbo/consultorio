from django import forms
from django.forms import widgets
from .models import Examen, Tipolente

class TipolenteForm(forms.ModelForm):
  class Meta:
    model = Tipolente
    fields = ('nombre', 'descripcion')

    widgets = {
      'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
    }

class ExamenForm(forms.ModelForm):
  class Meta:
    model = Examen
    fields = ('nombre', 'titulo', 'detalle')
    widgets = {
      'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'titulo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'detalle': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
    }