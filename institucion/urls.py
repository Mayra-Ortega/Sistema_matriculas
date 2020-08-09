from django.urls import path, include
from django.conf.urls import url
from institucion import views
# from django.contrib.auth import logout



urlpatterns = [
    # institucion
    path(r'institucion_create', views.institucion_create, name='institucion_create'),
    path(r'institucion_edit/<int:pk>/', views.institucion_edit, name='institucion_edit'),
    path(r'institucion_detail/<int:pk>/', views.InstitucionDetail.as_view(), name = 'institucion_detail'),
	path(r'institucion_list/', views.InstitucionList.as_view(), name = 'institucion_list'),
    # Ciclo
    path(r'ciclo_create', views.ciclo_create, name='ciclo_create'),
    path(r'ciclo_edit/<int:pk>/', views.ciclo_edit, name='ciclo_edit'),
    path(r'ciclo_detail/<int:pk>/', views.CicloDetail.as_view(), name = 'ciclo_detail'),
	path(r'ciclo_list/', views.CicloList.as_view(), name = 'ciclo_list'),
	path(r'ciclo_delete/<int:pk>/delete/', views.CicloDelete.as_view(), name='ciclo_delete'),
    # Curso
    path(r'curso_create', views.curso_create, name='curso_create'),
    path(r'curso_edit/<int:pk>/', views.curso_edit, name='curso_edit'),
    path(r'curso_detail/<int:pk>/', views.CursoDetail.as_view(), name = 'curso_detail'),
	path(r'curso_list/', views.CursoList.as_view(), name = 'curso_list'),
	path(r'curso_delete/<int:pk>/delete/', views.CursoDelete.as_view(), name='curso_delete'),

    # Paralelos
    path(r'paralelo_create', views.paralelo_create, name='paralelo_create'),
    path(r'paralelo_edit/<int:pk>/', views.paralelo_edit, name='paralelo_edit'),
    path(r'paralelo_detail/<int:pk>/', views.ParaleloDetail.as_view(), name = 'paralelo_detail'),
	path(r'paralelo_list/', views.ParaleloList.as_view(), name = 'paralelo_list'),
	path(r'paralelo_delete/<int:pk>/delete/', views.ParaleloDelete.as_view(), name='paralelo_delete'),

    # Preguntas PreguntasFrecuentes
    path(r'pregunta_create', views.pregunta_create, name='pregunta_create'),
    path(r'pregunta_edit/<int:pk>/', views.pregunta_edit, name='pregunta_edit'),
    path(r'pregunta_detail/<int:pk>/', views.PreguntaDetail.as_view(), name = 'pregunta_detail'),
	path(r'pregunta_list/', views.PreguntaList.as_view(), name = 'pregunta_list'),
	path(r'pregunta_delete/<int:pk>/delete/', views.PreguntaDelete.as_view(), name='pregunta_delete'),
]
