from django.contrib import admin

# Register your models here.

# ACA VAMOS A REGISTRAR LOS MODELS PARA QUE APAREZCAN EN EL PANEL ADMIN
from .models import Dieta, Rutina, Usuario, Dieta, Plan

# Creamos una clase que hereda de los modelos para indicar que queremos mostrar en el panel admin: REGISTRAR LA CLASE ABAJO!
class ClientesAdmin(admin.ModelAdmin):
    # lon campos a mostrar deben estar escritos tal cual estan declarados en el model de usuarios en este caso:
    list_display = ("nombre", "apellido", "vencido")
    # Para agregar campo de busqueda: por nombre y apellido
    search_fields = ("nombre", "apellido")


class DietaAdmin(admin.ModelAdmin):
    list_display = ("usr","dia1","dia2")    

# ADEMAS REGISTRAMOS CLIENTESADMIN!
admin.site.register(Usuario, ClientesAdmin)
admin.site.register(Rutina)
admin.site.register(Dieta, DietaAdmin)
admin.site.register(Plan)