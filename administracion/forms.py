from django import forms

from .models import IngresoSeguro, IngresoParticular, EgresoParticular

class IngresosParticularForm(forms.ModelForm):
    class Meta:
        model = IngresoParticular
        fields = ('fecha_inicio', 'fecha_fin')
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'date'})
        }

class IngresosParticularDepositoForm(forms.ModelForm):
    class Meta:
        model = IngresoParticular
        fields = ('fecha_deposito', 'photo')

class IngresosSeguroForm(forms.ModelForm):
    class Meta:
        model = IngresoSeguro
        fields = ('seguro', 'fecha_inicio', 'fecha_fin')
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'date'})
        }

class IngresosSeguroDepositoForm(forms.ModelForm):
    class Meta:
        model = IngresoSeguro
        fields = ('fecha_deposito', 'photo')

class EgresoParticularForm(forms.ModelForm):
    class Meta:
        model = EgresoParticular
        fields = ('fecha', 'monto', 'descripcion')