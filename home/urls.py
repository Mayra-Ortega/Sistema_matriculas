from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from home import views
# from django.contrib.auth import logout



urlpatterns = [
    # The home page
    path(r'', views.login, name='login'),
    path(r'index', views.index, name='index'),
    path(r'login', views.login, name='login'),
    url(r'logout', views.logout_view, name='logout'),
    # path(r'catalogo', views.catalogo, name='catalogo'),
    # path(r'nosotros', views.nosotros, name='nosotros'),
    # path(r'contacto', views.contacto, name='contacto'),
]
