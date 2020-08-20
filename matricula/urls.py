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
    path(r'desaprobar_matricula/<int:pk>/', views.desaprobar_matricula, name = 'desaprobar_matricula'),
    path(r'certificado_matricula/<int:pk>/', views.certificado_matricula, name = 'certificado_matricula'),
    path(r'matricula_delete/<int:pk>/', views.MatriculaDelete.as_view(), name = 'matricula_delete'),

    # Lista de Estudiantes
    path(r'form_estudiantes_filter/', views.form_estudiantes_filter, name = 'form_estudiantes_filter'),
    # Solicitud de ingreso
    path(r'solicitud_ingreso_create/', views.solicitud_ingreso_create, name = 'solicitud_ingreso_create'),
    path(r'solicitud_ingreso/', views.solicitud_ingreso, name = 'solicitud_ingreso'),
    path(r'solicitud_ingreso_list/', views.solicitud_ingreso_list, name = 'solicitud_ingreso_list'),
    path(r'solicitudes_pendientes_list/', views.solicitudes_pendientes_list, name = 'solicitudes_pendientes_list'),
    path(r'solicitudes_aprobadas_list/', views.solicitudes_aprobadas_list, name = 'solicitudes_aprobadas_list'),
    path(r'aprobar_solicitud/<int:pk>/', views.aprobar_solicitud, name = 'aprobar_solicitud'),
    path(r'ver_solicitud/<int:pk>/', views.ver_solicitud, name = 'ver_solicitud'),
    path(r'solicitud_delete/<int:pk>/', views.SolicitudIngresoDelete.as_view(), name = 'solicitud_delete'),
]
