from django.shortcuts import render, redirect
from .forms import *
from usuarios.models import *
from usuarios.views import get_user
from django.contrib import messages
from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy


# Create your views here.
def matricula_create(request):
    print(Matricula.objects.all())
    user = User.objects.get(username = request.user)
    try:
        estudiante = Estudiante.objects.get(user=user)
        hay_estudiante = True
    except Exception as e:
        hay_estudiante = False
    ciclo_actual = CicloLectivo.objects.get(ciclo_actual = True)
    paralelos = Paralelo.objects.all()
    form_matricula = MatriculaForm()
    if hay_estudiante == True:
        if request.method == 'POST':
            form_matricula = MatriculaForm(request.POST)
            if form_matricula.is_valid():
                matricula = form_matricula.save(commit=False)
                matricula.estudiante = estudiante
                matricula.ciclo_lectivo = ciclo_actual
                matricula.save()
                messages.info(request, "Tú solicitud de matrícula fue creada con éxito")
                messages.info(request, "Le recordamos que el paralelo seleccionado, no es definitivo y puede ser cambiado por la persona encargada de reubicar los alumnos de la manera más pertinente")
                return redirect('matricula:matricula_list')
            else:
                messages.error(request, institucion.errors)
                context = {
                    'form_matricula': form_matricula,
                    'paralelos': paralelos,
                }
        context = {
            'form_matricula': form_matricula,
            'paralelos': paralelos,
            'hay_estudiante': hay_estudiante,
        }
    else:
        context = {
            'hay_estudiante': hay_estudiante,
        }
    return render(request, 'matricula/matricula_form.html', context)

def matricula_edit(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    form_matricula = MatriculaForm(instance = matricula)
    hay_estudiante = True
    if request.method == 'POST':
        form_matricula = MatriculaForm(request.POST, instance = matricula)
        if form_matricula.is_valid():
            form_matricula.save()
            messages.info(request, "La matricula se editó con éxito")
            return redirect('matricula:matricula_list')
        else:
            messages.error(request, matricula.errors)
            context = {
                'form_matricula': form_matricula,
            }
            return render(request, 'matricula/matricula_form.html', context)

    context = {
        'form_matricula': form_matricula,
        'hay_estudiante': hay_estudiante,
    }
    return render(request, 'matricula/matricula_form.html', context)

class MatriculaList(ListView):
    model = Matricula
    def get_context_data(self):
        queryset = super(MatriculaList, self).get_queryset()
        user = User.objects.get(username = self.request.user)
        ciclo_lectivo = CicloLectivo.objects.get(ciclo_actual=True)
        try:
            estudiante = Estudiante.objects.get(user=user)
            matriculas = Matricula.objects.filter(estudiante = estudiante, ciclo_lectivo = ciclo_lectivo)
            print(matriculas)
            if matriculas.count() > 0:
                hay_matricula = True
            else:
                hay_matricula = False
        except Exception as e:
            hay_matricula = False
        context = {
            'hay_matricula': hay_matricula,
            'matriculas': matriculas,
        }
        return context

class MatriculaDetail(DetailView):
	model = Matricula

class MatriculaDelete(DeleteView):
    model = Matricula
    success_url = reverse_lazy('matricula:matriculas_pendientes_list')

def matriculas_pendientes_list(request):
    matriculas = Matricula.objects.filter(matricula_aceptada=False)
    context = {
        'matriculas': matriculas,
    }
    return render(request, 'matricula/matriculas_pendientes_list.html', context)

def matriculados_list(request):
    matriculas = Matricula.objects.filter(matricula_aceptada=True)
    context = {
        'matriculas': matriculas,
    }
    return render(request, 'matricula/matriculados_list.html', context)

def matricula_aprobacion(request, pk):
    matriculas = Matricula.objects.filter(matricula_aceptada=False)
    matricula = Matricula.objects.get(pk=pk)
    matricula.matricula_aceptada = True
    messages.info(request, "La matricula se aprobo con éxito")
    matricula.save()
    context = {
        'matriculas': matriculas,
    }
    return render(request, 'matricula/matriculas_pendientes_list.html', context)

def desaprobar_matricula(request, pk):
    matriculas = Matricula.objects.filter(matricula_aceptada=True)
    matricula = Matricula.objects.get(pk=pk)
    matricula.matricula_aceptada = False
    messages.info(request, "La matricula se desaprobo con éxito")
    matricula.save()
    context = {
        'matriculas': matriculas,
    }
    return render(request, 'matricula/matriculados_list.html', context)

def certificado_matricula(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    context = {
        'matricula': matricula,
    }
    return render(request, 'matricula/certificado_matricula.html', context)

def form_estudiantes_filter(request):
    form_filter_estudiantes = EstudiantesFilterForm()
    if request.method == 'POST':
        ciclo = request.POST.get('ciclo_lectivo')
        curso = request.POST.get('curso')
        paralelo = request.POST.get('paralelo')

        matriculas = Matricula.objects.filter(matricula_aceptada=True)
        estudiante = matriculas.first()

        if request.POST.get('ciclo_lectivo'):
            matriculas = matriculas.filter(ciclo_lectivo_id = ciclo)
        if request.POST.get('curso'):
            matriculas = matriculas.filter(curso_id = curso)
        if request.POST.get('paralelo'):
            matriculas = matriculas.filter(paralelo_id = paralelo)

        context = {
            'result_estudiantes_filter': matriculas,
            'estudiante': estudiante,
        }
        return render(request, 'matricula/list_estudiantes_filter.html', context)
    context = {
        'form_filter_estudiantes': form_filter_estudiantes,
    }
    return render(request, 'matricula/form_filter_estudiantes.html', context)


def solicitud_ingreso(request):

    return render(request, 'matricula/solicitud_ingreso.html')

def solicitud_ingreso_create(request):
    form_solicitud_ingreso = SolicitudIngresoForm(request)
    user = get_user(request)
    representante = Representante.objects.get(user = user)
    rector = User.objects.get(groups__name = 'Rector')
    print(rector)
    if request.method == 'POST':
        form_solicitud_ingreso = SolicitudIngresoForm(request, request.POST)
        if form_solicitud_ingreso.is_valid():
            solicitud = form_solicitud_ingreso.save(commit = False)
            solicitud.representante = representante
            solicitud.rector = rector
            solicitud.save()
            messages.info(request, "La solicitud se envio con éxito")
            return redirect('matricula:solicitud_ingreso_list')
    context = {
        'form_solicitud_ingreso': form_solicitud_ingreso,
    }
    return render(request, 'matricula/solicitud_form.html', context)

def solicitud_ingreso_list(request):
    user = get_user(request)
    representante = Representante.objects.get(user = user)
    solicitudes = SolicitudIngreso.objects.filter(representante=representante)
    context = {
        'solicitudes':solicitudes
    }
    return render(request, 'matricula/solicitudes_list.html', context)

def solicitudes_pendientes_list(request):
    solicitudes = SolicitudIngreso.objects.filter(aprobacion = False)
    context = {
        'solicitudes':solicitudes
    }
    return render(request, 'matricula/solicitudes_pendientes_list.html', context)

def solicitudes_aprobadas_list(request):
    solicitudes = SolicitudIngreso.objects.filter(aprobacion = True)
    context = {
        'solicitudes':solicitudes
    }
    return render(request, 'matricula/solicitudes_pendientes_list.html', context)

def aprobar_solicitud(request, pk):
    solicitud = SolicitudIngreso.objects.get(pk=pk)
    solicitud.aprobacion = True
    solicitud.f_aceptacion = date.today()
    solicitud.save()
    messages.info(request, "La solicitud se aprobo con éxito")
    return redirect('matricula:solicitudes_pendientes_list')

def ver_solicitud(request, pk):
    solicitud = SolicitudIngreso.objects.get(pk=pk)
    context = {
        'solicitud':solicitud
    }
    return render(request, 'matricula/solicitud_ingreso.html', context)
