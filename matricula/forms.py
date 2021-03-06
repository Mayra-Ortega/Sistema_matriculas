from django import forms
from .models import *
from institucion.models import *
class MatriculaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        # Get tecnicos select field
        ciclo_actual = CicloLectivo.objects.get(ciclo_actual = True)
        cursos = Curso.objects.filter(ciclo_lectivo = ciclo_actual)
        self.fields['curso'].queryset = cursos
        paralelos = Paralelo.objects.filter(curso__ciclo_lectivo = ciclo_actual)
        self.fields['paralelo'].queryset = paralelos
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


class SolicitudIngresoForm(forms.ModelForm):
    class Meta:
        model = SolicitudIngreso
        fields = (
            'estudiante',
            'ciclo_lectivo',
            'curso',
            'paralelo',
            'tipo_matricula',
            'viene_otra_institucion',
        )
    def __init__(self, request, *args, **kwargs):
        super(SolicitudIngresoForm, self).__init__(*args, **kwargs)
        usuario = User.objects.get(username = request.user)
        ciclo_lectivo = CicloLectivo.objects.get(ciclo_actual = True)
        self.fields['ciclo_lectivo'].initial = ciclo_lectivo
        cursos = Curso.objects.filter(ciclo_lectivo = ciclo_lectivo)
        self.fields['curso'].queryset = cursos
        paralelos = Paralelo.objects.filter(curso__ciclo_lectivo = ciclo_lectivo)
        self.fields['paralelo'].queryset = paralelos
        estudiantes = Estudiante.objects.all()
        representante = Padres.objects.get(representante_padres__user = usuario)
        print('representante')
        print(representante)
        print('representante')
        representados = Estudiante.objects.filter(padres_estudiante__usuario__ci_ruc = representante.usuario.ci_ruc, padres_estudiante__is_representante = True)
        print(representados)
        print('representante')
        self.fields['estudiante'].queryset = representados
