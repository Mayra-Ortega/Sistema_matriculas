from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
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
            estudiante.institucion = Institucion.objects.all().first()
            estudiante.save()
            messages.info(request, "Los datos del estudiante se guardaron con éxito")
            return redirect('usuarios:mis_datos_list')

    context = {
        'form_usuario': form_usuario,
        'form_estudiante': form_estudiante,
    }
    return render(request, 'usuarios/mis_datos.html', context)

def mis_datos_list(request):
    user = get_user(request)
    mis_datos = Estudiante.objects.filter(user=user)
    hay_datos = mis_datos.count()
    context = {
        'mis_datos': mis_datos,
        'hay_datos': hay_datos,
    }
    return render(request, 'usuarios/mis_datos_list.html', context)

def mis_datos_edit(request, pk):
    estudiante = Estudiante.objects.get(pk = pk)
    usuario = Usuario.objects.get(ci_ruc = estudiante.usuario.ci_ruc)
    form_usuario = UsuarioForm(instance = usuario)
    form_estudiante = EstudianteForm(instance = estudiante)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance = usuario)
        form_estudiante = EstudianteForm(request.POST, request.FILES, instance = estudiante)
        if form_usuario.is_valid() and form_estudiante.is_valid():
            usuario = form_usuario.save()
            estudiante = form_estudiante.save(commit=False)
            estudiante.user = User.objects.get(username = request.user)
            estudiante.usuario = usuario
            estudiante.institucion = Institucion.objects.all().first()
            estudiante.save()
            messages.info(request, "Los datos del estudiante se editaron con éxito")
            return redirect('usuarios:mis_datos_list')

    context = {
        'form_usuario': form_usuario,
        'form_estudiante': form_estudiante,
    }
    return render(request, 'usuarios/mis_datos.html', context)



class MisDatosDetail(DetailView):
	model = Estudiante
# falta template de este no se lo puso por seguridad.
class MisDatosDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('usuarios:mis_datos_list')


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
                # try:
                #     usuario_existente = Usuario.objects.get(ci_ruc = form_usuario.ci_ruc)
                #     usuario_existe = True
                # except Exception as e:
                #     usuario_existe = False
                # if usuario_existe == True:
                #     usuario_existente.padres_estudiante.add(estudiante)
                #     messages.info(request, "Los datos de la madre del estudiante se guardaron con éxito......")
                # else:
                usuario = form_usuario.save()
                madre = form_madre.save(commit=False)
                madre.padres_estudiante = estudiante
                madre.usuario = usuario
                madre.padres_familia = 'M'
                madre.parentesco = Parentesco.objects.get(parentesco = 'Madre')
                madre.save()
                messages.info(request, "Los datos de la madre del estudiante se guardaron con éxito")
                return redirect('usuarios:datos_padres_list')
        context = {
            'form_madre': form_madre,
            'form_usuario': form_usuario,
            'hay_estudiante': hay_estudiante,
        }
    else:
        context = {
            'hay_estudiante': hay_estudiante,
        }
    return render(request, 'usuarios/madre_form.html', context)

def datos_madre_edit(request, pk):
    madre = Padres.objects.get(pk=pk)
    usuario_madre = Usuario.objects.get(ci_ruc = madre.usuario.ci_ruc)
    form_usuario = UsuarioForm(instance = usuario_madre)
    form_madre = PadresForm(instance= madre)
    hay_estudiante = True
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance=usuario_madre)
        form_madre = PadresForm(request.POST, instance=madre)
        if form_usuario.is_valid() and form_madre.is_valid():
            usuario = form_usuario.save()
            madre = form_madre.save()
            messages.info(request, "Los datos de la madre del estudiante se editaron con éxito")
            return redirect('usuarios:datos_padres_list')
    context = {
        'form_madre': form_madre,
        'form_usuario': form_usuario,
        'hay_estudiante': hay_estudiante,
    }

    return render(request, 'usuarios/madre_form.html', context)


def datos_padres_list(request):
    user_actual = get_user(request)
    group = Group.objects.get(name= "Representante")
    user = User.objects.filter(groups = group)
    try:
        estudiante = Estudiante.objects.get(user=user_actual)
        hay_estudiante = True
    except Exception as e:
        hay_estudiante = False
        estudiante = None

    parentesco = Parentesco.objects.get(parentesco='Madre')
    padres = Padres.objects.filter(padres_estudiante = estudiante)
    hay_user_representante = False
    for representante in padres:
        if representante.is_representante == True:
            try:
                representante = Representante.objects.get(representante=representante)
                hay_user_representante = True
            except Exception as e:
                hay_user_representante = False
    hay_datos_madre = padres.filter(padres_familia = 'M').count()
    hay_datos_padre = padres.filter(padres_familia = 'P').count()
    context = {
        'padres': padres,
        'hay_datos_madre': hay_datos_madre,
        'hay_datos_padre': hay_datos_padre,
        'hay_user_representante': hay_user_representante,
        'hay_estudiante': hay_estudiante,
    }
    return render(request, 'usuarios/datos_padres_list.html', context)

class DatosPadresDetail(DetailView):
	model = Padres

def datos_padres_delete(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'usuarios/confirm_detele_padres.html', context)

def confirm_detele_padres(request, pk):
    padre = Padres.objects.get(pk=pk)
    usuario_padre = Usuario.objects.filter(ci_ruc = padre.usuario.ci_ruc).first()
    usuario_padre.delete()
    padre.delete()
    messages.info(request, "Los datos se eliminaron con éxito")
    return redirect('usuarios:datos_padres_list')
    return render(request, 'usuarios/datos_padres_list.html')

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
                return redirect('usuarios:datos_padres_list')
        context = {
            'form_padre': form_padre,
            'form_usuario': form_usuario,
            'hay_estudiante': hay_estudiante
        }
    else:
        context = {
            'hay_estudiante': hay_estudiante
        }
    return render(request, 'usuarios/padre_form.html', context)

def datos_padre_edit(request, pk):
    padre = Padres.objects.get(pk=pk)
    usuario_padre = Usuario.objects.filter(ci_ruc = padre.usuario.ci_ruc).first()
    form_usuario = UsuarioForm(instance = usuario_padre)
    form_padre = PadresForm(instance= padre)
    hay_estudiante = True
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance=usuario_padre)
        form_padre = PadresForm(request.POST, instance=padre)
        if form_usuario.is_valid() and form_padre.is_valid():
            usuario = form_usuario.save()
            padre = form_padre.save()
            messages.info(request, "Los datos del padre del estudiante se editaron con éxito")
            return redirect('usuarios:datos_padres_list')
    context = {
        'form_padre': form_padre,
        'form_usuario': form_usuario,
        'hay_estudiante': hay_estudiante,
    }

    return render(request, 'usuarios/padre_form.html', context)

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
                    return redirect('usuarios:datos_padres_list')
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
                    return redirect('usuarios:datos_padres_list')
            context = {
                'form_register': form_register,
                'hay_representante': hay_representante,
                'hay_estudiante': hay_estudiante,
            }
    else:
        context = {
            'hay_estudiante': hay_estudiante,
        }
    return render(request, 'usuarios/representante_form.html', context)

def datos_representante_edit(request, pk):
    representante = Padres.objects.get(pk=pk)
    usuario_representante = Usuario.objects.get(ci_ruc = representante.usuario.ci_ruc)
    form_usuario = UsuarioForm(instance = usuario_representante)
    form_representante = RepresentanteForm(instance= representante)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance=usuario_representante)
        form_representante = RepresentanteForm(request.POST, instance=representante)
        if form_usuario.is_valid() and form_representante.is_valid():
            usuario = form_usuario.save()
            representante = form_representante.save()
            messages.info(request, "Los datos del representante del estudiante se editaron con éxito")
            return redirect('usuarios:datos_representantes_list')
    context = {
        'form_representante': form_representante,
        'form_usuario': form_usuario,
    }

    return render(request, 'usuarios/representante_edit.html', context)
