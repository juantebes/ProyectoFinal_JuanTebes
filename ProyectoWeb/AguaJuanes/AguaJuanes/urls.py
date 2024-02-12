"""
URL configuration for AguaJuanes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Clientes.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('about/',about,name="about"),
    path('admin/', admin.site.urls),
    
    
    path('vercliente/',ver_cliente,name="ver_clientes"),
    
    
    path('',inicio,name="inicio"),
    
    #URLs para crear nuevos datos
    path('agregarproductos/',agregarProducto, name="agregarproductos"), #url,vista
    path("buscarProducto",busquedaProducto,name="buscarproducto"),
    path("resultados/",resultados,name="ResultadosBusqueda"),
    path('agregarcliente/',agregarCliente, name="agregarcliente"),
    
    path('editarcliente/<clienteNombre>', editarCliente, name = 'editarcliente'),
    
    path('login/',inicio_sesion, name = 'Iniciar sesion'),
    path('signup/',registro, name = 'Registrar usuario'),
    path("logout/",cerrar_sesion,name="Cerrar sesion"),
    path('edit/',editar_perfil, name = 'Editar usuario'),
    
    #CRUD CLIENTES USANDO CLASES 
    path('cliente/list/',ListaCliente.as_view(), name = "ClienteLeer"),
    path("cliente/<int:pk>",DetalleCliente.as_view(), name = "ClienteDetalle"),
    
    
    
    ]
    
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)