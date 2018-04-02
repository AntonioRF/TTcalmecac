from django import forms
from apps.edificio.models import Edificio

class EdificioForm(forms.ModelForm):

	class Meta:
		model = Edificio

		fields = [
			'nombre',
			'nivel',
			'tipo',
		]
		labels = {
			'nombre': 'Nombre',
			'nivel': 'Nivel',
			'tipo': 'Tipo',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'nivel': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.RadioSelect(),
		}