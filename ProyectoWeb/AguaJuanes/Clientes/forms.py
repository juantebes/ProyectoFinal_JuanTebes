from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class FormularioCliente(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    direccion=forms.CharField(max_length=20)
    telefono=forms.IntegerField()

class addproductform(forms.Form):
    nombre=forms.CharField(max_length=20)
    descripcion=forms.CharField(max_length=50)
    numero=forms.IntegerField()

class RegistrarUsuario(UserCreationForm):
     username=forms.CharField(label="Nombre de usuario")
     email=forms.EmailField()
     password1=forms.CharField(label="Contraseña")
     password2=forms.CharField(label="Reeingrese su contraseña")
     first_name=forms.CharField(label="Nobre")
     last_name=forms.CharField(label="Apellido")
     
     class Meta:
         model=User 
         fields=["username","email","password1","password2","first_name","last_name"]
     
    
