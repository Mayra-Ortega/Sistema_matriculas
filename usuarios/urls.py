from django.urls import path, include
from django.conf.urls import url
from usuarios import views
# from django.contrib.auth import logout



urlpatterns = [
#Datos del estudiante
    path(r'mis_datos', views.mis_datos, name='mis_datos'),
    path(r'mis_datos_list', views.mis_datos_list, name='mis_datos_list'),
    path(r'mis_datos_detail/<int:pk>/', views.MisDatosDetail.as_view(), name = 'mis_datos_detail'),
    path(r'mis_datos_edit/<int:pk>/', views.mis_datos_edit, name = 'mis_datos_edit'),
	path(r'mis_datos_delete/<int:pk>/delete/', views.MisDatosDelete.as_view(), name='mis_datos_delete'),

    #Datos de la madre del estudiante
    path(r'datos_madre', views.datos_madre, name='datos_madre'),
    path(r'datos_madre_edit/<int:pk>/', views.datos_madre_edit, name='datos_madre_edit'),
    path(r'datos_padres_list', views.datos_padres_list, name='datos_padres_list'),
    path(r'datos_padres_detail/<int:pk>/', views.DatosPadresDetail.as_view(), name='datos_padres_detail'),
    path(r'datos_padres_delete/<int:pk>/', views.datos_padres_delete, name='datos_padres_delete'),
    path(r'confirm_detele_padres/<int:pk>/', views.confirm_detele_padres, name='confirm_detele_padres'),
    path(r'datos_padre', views.datos_padre, name='datos_padre'),
    path(r'datos_padre_edit/<int:pk>/', views.datos_padre_edit, name='datos_padre_edit'),
    path(r'datos_representante', views.datos_representante, name='datos_representante'),
    path(r'datos_representante_edit/<int:pk>/', views.datos_representante_edit, name='datos_representante_edit'),
]
