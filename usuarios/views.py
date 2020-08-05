from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.forms import *

# Create your views here.
def mis_datos(request):
    form_usuario = UsuarioForm()
    form_estudiante = EstudianteForm()
    # usuario_actual = User.objects.get(username = request.user)
    # print(usuario_actual)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        form_estudiante = EstudianteForm(request.POST, request.FILES)
        if form_usuario.is_valid() and form_estudiante.is_valid():
            usuario = form_usuario.save()
            estudiante = form_estudiante.save(commit=False)
            estudiante.user = User.objects.get(username = request.user)
            estudiante.usuario = usuario
            estudiante.institucion = Institucion.objects.get(nombre='San Juan Bautista')
            estudiante.save()
            print("si guardo datos del estudiante")
            return redirect('index')

    context = {
        'form_usuario': form_usuario,
        'form_estudiante': form_estudiante,
    }
    return render(request, 'usuario/mis_datos.html', context)

def datos_madre(request):
    form_usuario = UsuarioForm()
    form_madre = PadresForm()
    estudiante_user =  User.objects.get(username = request.user)
    estudiante = Estudiante.objects.get(user = estudiante_user)
    print(estudiante)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        form_madre = PadresForm(request.POST)
        if form_usuario.is_valid() and form_madre.is_valid():
            usuario = form_usuario.save()
            madre = form_madre.save(commit=False)
            madre.padres_estudiante = estudiante
            madre.usuario = usuario
            madre.padres_familia = 'M'
            madre.parentesco = Parentesco.objects.get(parentesco = 'Madre')
            madre.save()
            print("si guardo datos de la madre")
            return redirect('index')
    context = {
        'form_madre': form_madre,
        'form_usuario': form_usuario,
    }
    return render(request, 'usuario/madre_form.html', context)

def datos_padre(request):
    form_usuario = UsuarioForm()
    form_padre = PadresForm()
    estudiante_user =  User.objects.get(username = request.user)
    estudiante = Estudiante.objects.get(user = estudiante_user)
    print(estudiante)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        form_padre = PadresForm(request.POST)
        if form_usuario.is_valid() and form_padre.is_valid():
            usuario = form_usuario.save()
            padre = form_padre.save(commit=False)
            padre.padres_estudiante = estudiante
            padre.usuario = usuario
            padre.parentesco = Parentesco.objects.get(parentesco = 'Padre')
            padre.save()
            print("si guardo datos de la padre")
            return redirect('index')
    context = {
        'form_padre': form_padre,
        'form_usuario': form_usuario,
    }
    return render(request, 'usuario/padre_form.html', context)

def datos_representante(request):
    form_usuario = UsuarioForm()
    form_representante = RepresentanteForm()
    estudiante_user =  User.objects.get(username = request.user)
    estudiante = Estudiante.objects.get(user = estudiante_user)
    print(estudiante)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        form_representante = RepresentanteForm(request.POST)
        if form_usuario.is_valid() and form_representante.is_valid():
            usuario = form_usuario.save()
            representante = form_representante.save(commit=False)
            representante.padres_estudiante = estudiante
            representante.usuario = usuario
            representante.save()
            print("si guardo datos del representante")
            return redirect('index')
    context = {
        'form_representante': form_representante,
        'form_usuario': form_usuario,
    }
    return render(request, 'usuario/representante_form.html', context)
