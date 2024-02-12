from django.shortcuts import render
from Clientes.models import Cliente
from django.http import HttpResponse
from Clientes.models import *
from Clientes.forms import * 
from Clientes.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    return render(request,"inicio.html")

def ver_cliente(request):
    mis_clientes=Cliente.objects.all() #obtengo todos los datos de mi tabla cliente 
    info={"clientes":mis_clientes}
    return render(request,"ver_clientes.html",info)

@login_required
def agregarCliente(request):
    if request.method== "POST":
        addclient=FormularioCliente(request.POST)
        if addclient.is_valid(): #ver si la informacion cargada es valida 
            info1=addclient.cleaned_data #convertir en un diccionario 
            cliente1=Cliente(nombre=info1["nombre"],apellido=info1["apellido"],direccion=info1["direccion"],telefono=info1["telefono"])
            cliente1.save()
            return render(request,"inicio.html")
    else:
        addclient=FormularioCliente()
    return render (request,"agregarCliente.html",{"formcliente":addclient})

def editarCliente(request, clienteNombre):
    clienteSeleccionado = Cliente.objects.filter(nombre=clienteNombre)
    if request.method== "POST":
        addclient=FormularioCliente(request.POST)
        if addclient.is_valid(): #ver si la informacion cargada es valida 
            info1=addclient.cleaned_data #convertir en un diccionario
            clienteSeleccionado.nombre = info1["nombre"]
            clienteSeleccionado.apellido = info1["apellido"]
            clienteSeleccionado.direccion = info1["direccion"]
            clienteSeleccionado.telefono = info1["telefono"]
            clienteSeleccionado.save()
            return render(request,"inicio.html")
    else:
        addclient=FormularioCliente()
    return render (request,"editarCliente.html",{"formcliente":addclient})

@login_required
def agregarProducto(request):
    if request.method== "POST":
        addproduct=addproductform(request.POST)
        if addproduct.is_valid(): #ver si la informacion cargada es valida 
            info=addproduct.cleaned_data #convertir en un diccionario 
            producto1=Productos(nombre_producto=info["nombre"],descripcion_producto=info["descripcion"],numero_producto=info["numero"])
            producto1.save()
            return render(request,"inicio.html")
    else:
        addproduct=addproductform()
    return render (request,"agregarproducto.html",{"formprod":addproduct})

def busquedaProducto(request):
    return render(request,"busquedaProducto.html")

def resultados(request):
    if request.method=="GET":
        numero_producto_pedido=request.GET["numero"]
        resultados_productos=Productos.objects.filter(numero_producto__icontains=numero_producto_pedido)
        return render (request,"resultados.html",{"productos":resultados_productos})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)


#Vistas register
def registro(request):
    if request.method=="POST":
        formulario=RegistrarUsuario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            usuario=info["username"]
            formulario.save()
            return render (request,"inicio.html",{"mensaje":f"Bienvenido {usuario}"})
    else:
        formulario=RegistrarUsuario()  
    return render (request,"registro/registrar_usuario.html",{"formu":formulario})

def editar_perfil(request):
    usuario_actual=request.user #obtengo el usuario actualmente registrado
    if request.method=="POST":
        formulario=RegistrarUsuario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            usuario_actual.first_name=info["first_name"]
            usuario_actual.last_name=info["last_name"]
            usuario_actual.email=info["email"]
            usuario_actual.save()
            return render (request,"inicio.html")
    else:
        formulario=RegistrarUsuario(initial={"first_name":usuario_actual.first_name})  
    return render (request,"registro/editar_usuario.html",{"formu":formulario})
    
    
def inicio_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            usuario = info["username"]
            contra = info["password"]
            usuario_actual= authenticate(username=usuario, password=contra)
 
            if usuario_actual is not None:
                login(request, usuario_actual)
                
                return render(request,"inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
            else:
                         
                return render(request,"inicio.html", {"mensaje":"Error, datos incorrectos"} )
 
    else:
        formulario = AuthenticationForm()
    
    return render(request,"registro/inicio_sesion.html", {"formu":formulario} )

def cerrar_sesion(request):
    logout(request)
    return render(request,"registro/cerrar_sesion.html")

def about(request):
    return render(request,"about.html")

class ListaCliente(ListView):
    model=Cliente

class DetalleCliente(DetailView):
    model=Cliente

class CrearCliente(CreateView):
    model=Cliente
    success_url="/cliente/list"
    fields=["nombre","apellido","direccion","telefono"]

class ActualizarCliente(UpdateView):
    model=Cliente
    success_url="/cliente/list"
    fields=["nombre","apellido","direccion","telefono"]

class BorrarCliente(DeleteView):
    model=Cliente
    success_url="/cliente/list"
    

