from django import forms
from django.forms import fields, widgets
from .models import Evolucion

class EvolucionForms(forms.ModelForm):
    class Meta:
        model = Evolucion
        fields = '__all__'
        widgets = {
            'dias_domo': forms.NumberInput(attrs={'class':'form-control', 'readonly':'true'}),
            'nro_cama': forms.NumberInput(attrs={'class':'form-control'}),
            'analisis': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'plan': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }
