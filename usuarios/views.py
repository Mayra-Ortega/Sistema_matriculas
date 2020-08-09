from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.forms import *
from django.contrib import messages

def get_user(request):
    user = User.objects.get(username = request.user)
    return user
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

def mis_datos_list(request):
    user = get_user(request)
    mis_datos = Estudiante.objects.filter(user=user)
    context = {
        'mis_datos': mis_datos,
    }
    return render(request, 'matricula/mis_datos_list.html', context)

def datos_madre(request):
    form_usuario = UsuarioForm()
    form_madre = PadresForm()
    estudiante_user =  User.objects.get(username = request.user)
    try:
        estudiante = Estudiante.objects.get(user = estudiante_user)
        hay_estudiante = True
    except Exception as e:
        hay_estudiante = False
    if hay_estudiante == True:
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
            'hay_estudiante': hay_estudiante,
        }
    else:
        context = {
            'hay_estudiante': hay_estudiante,
        }
    return render(request, 'usuario/madre_form.html', context)

def datos_padre(request):
    form_usuario = UsuarioForm()
    form_padre = PadresForm()
    estudiante_user =  User.objects.get(username = request.user)
    try:
        estudiante = Estudiante.objects.get(user = estudiante_user)
        hay_estudiante = True
    except Exception as e:
        hay_estudiante = False
    if hay_estudiante == True:
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
            'hay_estudiante': hay_estudiante
        }
    else:
        context = {
            'hay_estudiante': hay_estudiante
        }
    return render(request, 'usuario/padre_form.html', context)

def datos_representante(request):
    estudiante_user =  User.objects.get(username = request.user)
    try:
        estudiante = Estudiante.objects.get(user = estudiante_user)
        hay_estudiante = True
    except Exception as e:
        hay_estudiante = False
    # formularios a presentar
    form_register = UserCreationForm()
    form_usuario = UsuarioForm()
    form_representante = RepresentanteForm()
    try:
        padres = Padres.objects.get(is_representante = True, padres_estudiante=estudiante)
        hay_representante = True
    except Exception as e:
        hay_representante = False
    if hay_estudiante == True:
        if hay_representante == False:
            if request.method == 'POST':
                form_register = UserCreationForm(request.POST)
                form_usuario = UsuarioForm(request.POST)
                form_representante = RepresentanteForm(request.POST)
                if form_register.is_valid() and form_usuario.is_valid() and form_representante.is_valid():
                    # user para logear a representante
                    user_representante = form_register.save(commit = False)
                    user_representante.is_staff = True
                    user_representante.save()
                    user_representante.groups.add(Group.objects.get(name="Representante"))
                    # datos del representante
                    usuario = form_usuario.save()
                    representante = form_representante.save(commit=False)
                    representante.padres_estudiante = estudiante
                    representante.usuario = usuario
                    representante.is_representante = True
                    representante.save()
                    representante = Representante.objects.create(representante = representante, user=user_representante)
                    messages.info(request, "Los datos del representante se guardaron correctamente")
                    messages.info(request, "Sr. Representante, recuerde ingresar con su usario y contraseña para llenar la solicitud de ingreso de su representado.")
                    return redirect('index')
            context = {
                'form_register': form_register,
                'form_representante': form_representante,
                'form_usuario': form_usuario,
                'hay_representante': hay_representante,
                'hay_estudiante': hay_estudiante,
            }
        else:
            if request.method == 'POST':
                form_register = UserCreationForm(request.POST)
                if form_register.is_valid():
                    user_representante = form_register.save(commit = False)
                    user_representante.is_staff = True
                    user_representante.save()
                    user_representante.groups.add(Group.objects.get(name="Representante"))
                    representante = Representante.objects.create(representante = padres, user=user_representante)
                    messages.info(request, "Los datos del representante se guardaron correctamente")
                    messages.info(request, "Sr. Representante, recuerde ingresar con su usario y contraseña para llenar la solicitud de ingreso de su representado.")
                    return redirect('index')
            context = {
                'form_register': form_register,
                'hay_representante': hay_representante,
                'hay_estudiante': hay_estudiante,
            }
    else:
        context = {
            'hay_estudiante': hay_estudiante,
        }
    return render(request, 'usuario/representante_form.html', context)
