from django import forms
from apps.espacio.models import Espacio

class EspacioForm(forms.ModelForm):

	class Meta:
		model = Espacio
		fields = [
			'numero',
			'nombre',
			'capacidad',
			'tipo',
			'acceso_discapacitados',
			'puede_utilizar',
			'observaciones',
		]
		labels = {
			'numero': 'Número',
			'nombre': 'Nombre',
			'capacidad': 'Capacidad',
			'tipo': 'Tipo',
			'acceso_discapacitados': '¿Cuenta con acceso para discapacitados',
			'puede_utilizar': '¿Puede ser utilizado?',
			'observaciones': 'Observaciones',
		}
		widgets = {
			'numero': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'capacidad': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.TextInput(attrs={'class':'form-control'}),
			'acceso_discapacitados': forms.TextInput(attrs={'class':'form-control'}),
			'puede_utilizar': forms.TextInput(attrs={'class':'form-control'}),
			'observaciones': forms.Textarea(attrs={'class':'form-control'}),
		}