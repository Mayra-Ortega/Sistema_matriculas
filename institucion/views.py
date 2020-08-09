from django.shortcuts import render, redirect
from institucion.forms import *
from institucion.models import *
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

def institucion_create(request):
    form_institucion = InstitucionForm()
    if request.method == 'POST':
        form_institucion = InstitucionForm(request.POST)
        if form_institucion.is_valid():
            form_institucion.save()
            return redirect('index')
    context = {
        'form_institucion': form_institucion,
    }
    return render(request, 'institucion/institucion_form.html', context)

def institucion_edit(request, pk):
    institucion = Institucion.objects.get(pk=pk)
    form_institucion = InstitucionForm(instance = institucion)
    if request.method == 'POST':
        form_institucion = InstitucionForm(request.POST, instance = institucion)
        if form_institucion.is_valid():
            form_institucion.save()
            messages.info(request, "La institución se editó con éxito")
            return redirect('institucion:institucion_list')
        else:
            messages.error(request, institucion.errors)
            context = {
                'form_institucion': form_institucion,
            }
            return render(request, 'institucion/institucion_form.html', context)

    context = {
        'form_institucion': form_institucion,
    }
    return render(request, 'institucion/institucion_form.html', context)

class InstitucionList(ListView):
	model = Institucion

class InstitucionDetail(DetailView):
	model = Institucion

def ciclo_create(request):
    form_ciclo = CicloForm()
    institucion = Institucion.objects.last()
    if request.method == 'POST':
        form_ciclo = CicloForm(request.POST)
        if form_ciclo.is_valid():
            ciclo = form_ciclo.save()
            institucion_ciclo = InstitucionCicloLectivo.objects.create(institucion=institucion, ciclo_lectivo=ciclo)
            return redirect('institucion:ciclo_list')
    context = {
        'form_ciclo': form_ciclo,
    }
    return render(request, 'institucion/ciclo_form.html', context)

def ciclo_edit(request, pk):
    ciclo = CicloLectivo.objects.get(pk=pk)
    form_ciclo = CicloForm(instance = ciclo)
    if request.method == 'POST':
        form_ciclo = CicloForm(request.POST, instance = ciclo)
        if form_ciclo.is_valid():
            form_ciclo.save()
            messages.info(request, "El ciclo se editó con éxito")
            return redirect('institucion:ciclo_list')
        else:
            messages.error(request, ciclo.errors)
            context = {
                'form_ciclo': form_ciclo,
            }
            return render(request, 'institucion/ciclo_form.html', context)

    context = {
        'form_ciclo': form_ciclo,
    }
    return render(request, 'institucion/ciclo_form.html', context)

class CicloList(ListView):
	model = CicloLectivo

class CicloDetail(DetailView):
	model = CicloLectivo

class CicloDelete(DeleteView):
    model = CicloLectivo
    success_url = reverse_lazy('institucion:ciclo_list')


def curso_create(request):
    form_curso = CursoForm()
    if request.method == 'POST':
        form_curso = CursoForm(request.POST)
        if form_curso.is_valid():
            form_curso.save()
            messages.info(request, "El curso se creo con éxito")
            return redirect('institucion:curso_list')
        else:
            messages.error(request, curso.errors)
            context = {
                'form_curso': form_curso,
            }
    context = {
        'form_curso': form_curso,
    }
    return render(request, 'institucion/curso_form.html', context)

def curso_edit(request, pk):
    curso = Curso.objects.get(pk=pk)
    form_curso = CursoForm(instance = curso)
    if request.method == 'POST':
        form_curso = CursoForm(request.POST, instance = curso)
        if form_curso.is_valid():
            form_curso.save()
            messages.info(request, "El curso se editó con éxito")
            return redirect('institucion:curso_list')
        else:
            messages.error(request, curso.errors)
            context = {
                'form_curso': form_curso,
            }
            return render(request, 'institucion/curso_form.html', context)

    context = {
        'form_curso': form_curso,
    }
    return render(request, 'institucion/curso_form.html', context)

class CursoList(ListView):
	model = Curso

class CursoDetail(DetailView):
	model = Curso

class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('institucion:curso_list')

def paralelo_create(request):
    form_paralelo = ParaleloForm()
    if request.method == 'POST':
        form_paralelo = ParaleloForm(request.POST)
        if form_paralelo.is_valid():
            form_paralelo.save()
            messages.info(request, 'El paralelo se creo con éxito.')
            return redirect('institucion:paralelo_list')
        else:
            messages.error(request, paralelo.errors)
            context = {
                'form_paralelo': form_paralelo,
            }
    context = {
        'form_paralelo': form_paralelo,
    }
    return render(request, 'institucion/paralelo_form.html', context)

def paralelo_edit(request, pk):
    paralelo = Paralelo.objects.get(pk=pk)
    form_paralelo = ParaleloForm(instance = paralelo)
    if request.method == 'POST':
        form_paralelo = ParaleloForm(request.POST, instance = paralelo)
        if form_paralelo.is_valid():
            form_paralelo.save()
            messages.info(request, "El paralelo se editó con éxito")
            return redirect('institucion:paralelo_list')
        else:
            messages.error(request, paralelo.errors)
            context = {
                'form_paralelo': form_paralelo,
            }
            return render(request, 'institucion/paralelo_form.html', context)

    context = {
        'form_paralelo': form_paralelo,
    }
    return render(request, 'institucion/paralelo_form.html', context)

class ParaleloList(ListView):
	model = Paralelo

class ParaleloDetail(DetailView):
	model = Paralelo

class ParaleloDelete(DeleteView):
    model = Paralelo
    success_url = reverse_lazy('institucion:paralelo_list')

def pregunta_create(request):
    form_pregunta = PreguntaFrecuenteForm()
    if request.method == 'POST':
        form_pregunta = PreguntaFrecuenteForm(request.POST)
        if form_pregunta.is_valid():
            form_pregunta.save()
            messages.info(request, 'La pregunta se creo con éxito.')
            return redirect('institucion:pregunta_list')
        else:
            messages.error(request, pregunta.errors)
            context = {
                'form_pregunta': form_pregunta,
            }
    context = {
        'form_pregunta': form_pregunta,
    }
    return render(request, 'institucion/preguntafrecuente_form.html', context)

def pregunta_edit(request, pk):
    pregunta = PreguntaFrecuente.objects.get(pk=pk)
    form_pregunta = PreguntaFrecuenteForm(instance = pregunta)
    if request.method == 'POST':
        form_pregunta = PreguntaFrecuenteForm(request.POST, instance = pregunta)
        if form_pregunta.is_valid():
            form_pregunta.save()
            messages.info(request, "La pregunta se editó con éxito")
            return redirect('institucion:pregunta_list')
        else:
            messages.error(request, pregunta.errors)
            context = {
                'form_pregunta': form_pregunta,
            }
            return render(request, 'institucion/preguntafrecuente_form.html', context)

    context = {
        'form_pregunta': form_pregunta,
    }
    return render(request, 'institucion/preguntafrecuente_form.html', context)


class PreguntaList(ListView):
	model = PreguntaFrecuente

class PreguntaDetail(DetailView):
	model = PreguntaFrecuente

class PreguntaDelete(DeleteView):
    model = PreguntaFrecuente
    success_url = reverse_lazy('institucion:pregunta_list')
