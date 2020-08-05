from django import forms
from .models import *

class MatriculaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        # Get tecnicos select field
        ciclo_actual = CicloLectivo.objects.get(ciclo_actual = True)
        cursos = Curso.objects.filter(ciclo_lectivo = ciclo_actual)
        self.fields['curso'].queryset = cursos
    class Meta:
        model = Matricula
        fields = (
            'curso',
            'paralelo',
            'observacion',
        )
        widgets = {
			'curso': forms.Select(attrs = {'onchange':'filtrarParalelos(this)'}),
			'paralelo': forms.Select(attrs = {'id':'choice_paralelo'}),
		}

class EstudiantesFilterForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = (
            'ciclo_lectivo',
            'curso',
            'paralelo',
        )
    def __init__(self, *args, **kwargs):
        super(EstudiantesFilterForm, self).__init__(*args, **kwargs)

        # Set required False
        self.fields['ciclo_lectivo'].required=False
        self.fields['curso'].required=False
        self.fields['paralelo'].required=False
