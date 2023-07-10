"""proyectoTaller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #----------------------------------------------------> Templates
    path('', views.index, name="paginacargaini"),
    path('salir/',views.salir, name='salir'),
    path('proyecto', views.proyecto, name="proyecto"),
    path('cambiodemotor', views.cambiomotor, name="cambiodemotor"),
    path('formulario', views.formulario, name="formulario"),
    path('equipo', views.equipo, name="equipo"),
    path('correo', views.correo, name="correo"),
    path('login', views.inicio, name="login"),
    path('clientes', views.home, name="clientes"),
    path('edicionfor', views.edifor, name="edicionfor"),
    path('registrarCliente/', views.registrarCliente),
    path('editarCliente/', views.editarCliente),
    path('edicionCliente/<rut>', views.edicionCliente),
    path('eliminarCliente/<rut>', views.eliminarCliente),
]   