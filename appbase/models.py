from ast import Return
from email.policy import default
from enum import unique
from tabnanny import verbose
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# PLANIFICACION DIARIA:
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
    
# AGREGAMOS MODEL PLANIFICACIONES POR SEMANA:
class RutinaSemanal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    activacion = models.TextField(max_length=500,blank=True)
    semana1 = models.TextField(max_length=500,blank=True)
    semana2 = models.TextField(max_length=500,blank=True)
    semana3 = models.TextField(max_length=500,blank=True)
    semana4 = models.TextField(max_length=500,blank=True)
    semana5 = models.TextField(max_length=500,blank=True)
    semana6 = models.TextField(max_length=500,blank=True)
    semana7 = models.TextField(max_length=500,blank=True)
    semana8 = models.TextField(max_length=500,blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True, blank=True)
    f_vencimiento = models.DateField(null=True, blank=True)
    cerca_vto = models.BooleanField(default=False)

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
        db_table = 'appbase_dieta'
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        ordering = ['id']

class Plan(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    dni = models.IntegerField(null=True, blank=False, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ocho = models.BooleanField(default=False, blank=True)
    doce = models.BooleanField(default=False, blank=True)
    full = models.BooleanField(default=False, blank=True)
    f_pago = models.DateField(default=False, blank=True)
    f_vencimiento = models.DateField(null=True, blank=True)
    asistencia = models.IntegerField(null=False, default=0)

    def __str__(self):
        return (f'{self.usr}')

