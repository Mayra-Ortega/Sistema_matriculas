from django.urls import path, include
from django.conf.urls import url
from matricula import views
# from django.contrib.auth import logout



urlpatterns = [
    # Matricula_estudiante
    path(r'matricula_create', views.matricula_create, name='matricula_create'),
    path(r'matricula_edit/<int:pk>/', views.matricula_edit, name='matricula_edit'),
    path(r'matricula_detail/<int:pk>/', views.MatriculaDetail.as_view(), name = 'matricula_detail'),
    path(r'matricula_list/', views.MatriculaList.as_view(), name = 'matricula_list'),

    # Matricula secretaria
    path(r'matriculas_pendientes_list/', views.matriculas_pendientes_list, name = 'matriculas_pendientes_list'),
    path(r'matriculados_list/', views.matriculados_list, name = 'matriculados_list'),
    path(r'matricula_aprobacion/<int:pk>/', views.matricula_aprobacion, name = 'matricula_aprobacion'),
    path(r'certificado_matricula/<int:pk>/', views.certificado_matricula, name = 'certificado_matricula'),

    # Lista de Estudiantes
    path(r'form_estudiantes_filter/', views.form_estudiantes_filter, name = 'form_estudiantes_filter'),
    # Solicitud de ingreso
    path(r'solicitud_ingreso_create/', views.solicitud_ingreso_create, name = 'solicitud_ingreso_create'),
    path(r'solicitud_ingreso/', views.solicitud_ingreso, name = 'solicitud_ingreso'),
]
