from django.urls import path, include
from django.conf.urls import url
from usuarios import views
# from django.contrib.auth import logout



urlpatterns = [
    path(r'mis_datos', views.mis_datos, name='mis_datos'),
    path(r'datos_madre', views.datos_madre, name='datos_madre'),
    path(r'datos_padre', views.datos_padre, name='datos_padre'),
    path(r'datos_representante', views.datos_representante, name='datos_representante'),
]
