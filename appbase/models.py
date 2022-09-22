from ast import Return
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    pago = models.DateField()
    vencido = models.BooleanField()
    plan = models.CharField(max_length=4)

    # Esta clase convierte la respuesta que esta como objeto a str para que se muestren los nombres
    # de los usuarios en el panel admin:
    def __str__(self):
        return (f"{self.nombre}  {self.apellido}")

class Rutina(models.Model):
    # Creamos la relacion entre rutinas tabla usuario django Auth_User que importamos arrriba:
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    activacion = models.TextField(max_length=500,blank=True)
    dia1 = models.TextField(max_length=500,blank=True)
    dia2 = models.TextField(max_length=500,blank=True)
    dia3 = models.TextField(max_length=500,blank=True)
    dia4 = models.TextField(max_length=500,blank=True)
    dia5 = models.TextField(max_length=500,blank=True)
    dia6 = models.TextField(max_length=500,blank=True)
    dia7 = models.TextField(max_length=500, blank=True)

    # nos va a devolver lo que formateemos por cada uno de los registros que tengamos en la tabla rutina:
    def __str__(self):
        return (f'{self.usuario}')
    
class Dieta(models.Model):
    # Creamos la relacion entre rutinas tabla usuario django Auth_User que importamos arrriba:
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    dia1 = models.TextField(max_length=500,blank=True)
    dia2 = models.TextField(max_length=500,blank=True)
    dia3 = models.TextField(max_length=500,blank=True)
    dia4 = models.TextField(max_length=500,blank=True)
    dia5 = models.TextField(max_length=500,blank=True)
    dia6 = models.TextField(max_length=500,blank=True)
    dia7 = models.TextField(max_length=500, blank=True)

    # nos va a devolver lo que formateemos por cada uno de los registros que tengamos en la tabla rutina:
    def __str__(self):
        return (f'{self.usr}')

    class Meta:
        db_table = 'dieta'
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        ordering = ['id']