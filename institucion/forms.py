from django import forms
from .models import *

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'


class CicloForm(forms.ModelForm):
    class Meta:
        model = CicloLectivo
        fields = '__all__'
        widgets = {
			'inicio': forms.DateInput(attrs = {'type':'Date'}),
			'fin': forms.DateInput(attrs = {'type':'Date'}),
		}

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class ParaleloForm(forms.ModelForm):
    class Meta:
        model = Paralelo
        fields = (
        'curso',
        'nombre',
        )

class PreguntaFrecuenteForm(forms.ModelForm):
    class Meta:
        model = PreguntaFrecuente
        fields = '__all__'
