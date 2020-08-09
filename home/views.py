# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from institucion.models import *
from usuarios.models import *
from matricula.models import *


# Create your views here.
def index(request):
    user = User.objects.get(username = request.user)
    preguntas = PreguntaFrecuente.objects.all()
    rol = user.groups.all().first()
    # consultamos el numero de estudiantes
    estudiantes = Estudiante.objects.all().count()
    # consultamos el numero de estudiantes matriculados
    matriculados = Matricula.objects.filter(matricula_aceptada=True).count()
    # consultamos el numero de estudiantes con matricula pendiente
    matriculas_pendientes = Matricula.objects.filter(matricula_aceptada=False).count()
    # consultamos el numero de cursos
    cursos = Curso.objects.all().count()
    # consultamos el numero de Paralelos
    paralelos = Paralelo.objects.all().count()
    # consultamos el numero de usuarios
    usuarios = User.objects.all().count()

    context = {
                'user': user,
                'rol': rol,
                'preguntas': preguntas,
                'estudiantes': estudiantes,
                'matriculados': matriculados,
                'matriculas_pendientes': matriculas_pendientes,
                'cursos': cursos,
                'paralelos': paralelos,
                'usuarios': usuarios,
            }
    return render(request, 'index.html', context)
    # Landing page de cada empresa

def login(request):
    form_register = UserCreationForm()
    form_login = AuthenticationForm()
    is_register = request.POST.get('is_register')
    print(is_register)
    if is_register == "True":
        if request.method == 'POST':
            form_register = UserCreationForm(request.POST)
            if form_register.is_valid():
                user = form_register.save(commit = False)
                user.is_staff = True
                user.save()
                user.groups.add(Group.objects.get(name="Estudiante"))
                username = form_register.cleaned_data.get('username')
                raw_password = form_register.cleaned_data.get('password1')
                # user = authenticate(username=username, password=raw_password)
                # index(request, user)
                return redirect('login')
        else:
            form_register = UserCreationForm()
            context = {
                        'login_register': login_register,
                        'form_login': form_login,
                    }
            return render(request, 'login.html', context)
    else:
        if request.method == "POST":
            form_login = AuthenticationForm(data=request.POST)
            if form_login.is_valid():
                print("entro")
                username = form_login.cleaned_data['username']
                password = form_login.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    do_login(request, user)
                    return redirect('index')
        else:
            context = {
                        'form_register': form_register,
                        'form_login': form_login,
                    }
            return render(request, 'login.html', context)
    context = {
                'form_register': form_register,
                'form_login': form_login,
            }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.
