from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()

class Productos(models.Model):
    def __str__(self):
        return f"{self.nombre_producto}"
    nombre_producto=models.CharField(max_length=20)
    descripcion_producto=models.CharField(max_length=20)
    numero_producto=models.IntegerField()

class AvatarImagen(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares",null=True,blank=True)
    
