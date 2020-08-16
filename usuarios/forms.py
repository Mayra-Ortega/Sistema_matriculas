from django import forms
from .models import *
import datetime
from django.utils import timezone

class DateInput(forms.DateInput):
	input_type = 'date'
	# initial = timezone.now()
	initial = datetime.date.today()

class TimeInput(forms.TimeInput):
	input_type = 'time'
	initial = timezone.now()

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = (
            'f_nacimiento',
            'lugar_nacimiento',
            'img_perfil',
        )
        exclude = ['user', 'usuario', 'institucion', 'rol']
        widgets = {
			'f_nacimiento': forms.DateInput(attrs = {'type':'Date'}),
		}
class PadresForm(forms.ModelForm):
	class Meta:
	    model = Padres
	    fields = (
			'is_representante',
			'nivel_educacion',
			'profesion',
		)

class RepresentanteForm(forms.ModelForm):
	class Meta:
	    model = Padres
	    fields = (
			'nivel_educacion',
			'profesion',
			'parentesco',
		)
