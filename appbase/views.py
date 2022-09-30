from contextvars import Context
from dataclasses import asdict
from multiprocessing import context
from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.http import HttpResponse
from django.contrib import messages # para mostrar mensajes flash
from django.contrib.auth import login, logout, authenticate # para manejar sesiones de usuarios registrados en DB
# Importamos rutina para poder acceder a los datos de la dn a traves de una consulta ORM
from .models import Rutina, Dieta, Plan,Usuario
from django.contrib.auth.models import User

# Create your views here.

# Clase basada en vista para la creacion de usuario:
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # importamos formulario provisto por django

# La clase VistaRegistro heredara de la clase View de django:
class VistaRegistro(View):

# Mostramos el formulario del registro:
    def get(self, request):
        form = UserCreationForm()
        return render(request, "appbase/registro.html", {"form": form}) # pasamos como parametro el formulario django

# Procesamos el formulario:
    def post(self, request):
        # pasamos los datos del formulario por post
        form = UserCreationForm(request.POST)
        # y verificamos que sea un formulario valido para guardarlo
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, f"Registro exitoso, bienvenido {nombre_usuario}!")
            # luego de comprobar, iniciamos sesion y redireccionamos al home:
            login(request, usuario)
            return redirect("home")
        else:
            # recorremos los mensajes capturados por django
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, "appbase/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, f'Tu sesion se cerro correctamente')
    return redirect("acceder")

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=passwd)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"Bienvenido de nuevo {nombre_usuario}")
                return redirect("home")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    # llamamos al formulario:
    form = AuthenticationForm()
    return render(request, "appbase/index.html", {"form": form})



def index(request):
    return render(request,'appbase/index.html')

def home(request):
    return render(request,'appbase/home.html')

def rutinas(request):
    if User.is_authenticated:
        # Obtenemos en la variable el id de usuario para luego filtrarlo:
        id_usuario = request.user.id
        # ayuda para saber id
        print(f'User ID: {id_usuario}')
        # filtramos por medio del id. La variable usuario_id corresponde a la relacion de la db creada por el model:
        rutinas = Rutina.objects.filter(usuario_id = f'{id_usuario}')
        print(rutinas)
        return render(request, 'appbase/rutinas.html', {'rutinas':rutinas})
        

def dietas(request):
    if User.is_authenticated:
        id_usr = request.user.id
        dieta = Dieta.objects.filter(usr_id = id_usr )
        print(dieta)
        return render(request, 'appbase/dietas.html', {'dieta': dieta})

def plan(request):
    # Obtenemos el id para actualizar los registros:
    if User.is_authenticated:    
        id_usr = request.user.id
        print(f'ID Usuario {id_usr}')
        
        # OBTENEMOS LOS REGISTROS PARA ESE USUARIO: SI NO TIENE REGISTROS DATA ERROR:
        # EN CADA CONSULTA A LA DB AGREGAR TRY EXCEPT, MOSTRAR PLANTILLA VACIA, E INFORMAR POR POPUP

        planes = Plan.objects.filter(usr_id = id_usr)
        # Filtramos fecha de pago, tipo plan y num asistencias y la pasamos como dict:
        for p in planes:
            ocho = p.ocho
            doce = p.doce
            full = p.full
            asistencias = p.asistencia
            pago = (p.f_pago)
            print(type(asistencias))
            print(f'Pago realizado {pago}')
            vencimiento = pago + timedelta(days = 30)
            # Actualizamos la BD con la fecha de vencimiento a traves de la foreignKey
            Plan.objects.filter(usr_id = id_usr).update(f_vencimiento = vencimiento)
            print (type(vencimiento))
            print(type(date.today()))
            # Pasamos el estado al front:
            if date.today() > vencimiento:
                vencido = 'Si'
            else:
                vencido = 'No'

            # FILTRAR USUARIO!

            # def clases(plan1, plan2):
            if ocho == True: 
                ocho = 8
                restantes = ocho - asistencias
                print(restantes)
                # return restantes
            elif doce == True:
                doce = 12
                restantes = doce - asistencias
                print(restantes)
                # return restantes
            elif full == True:
                restantes = 'Full'
                print(restantes)
                # return restantes
            
            # clases_plan = clases(ocho,doce)
            # if clases_plan == 8 | clases_plan == 12:
            #     restantes = clases_plan - asistencias
            #     return restantes
            # else:
            #     restantes = 'Full'
            #     return restantes

        return render(request, 'appbase/plan.html',{'f_pago': planes,'pago':pago,'vencido':vencido,'fecha_venc': vencimiento,'restantes': restantes,})

def control(request):
    # Obtenemos el dni ingresado por formulario:
    if request.POST:
        dni = request.POST['dni']
        dni = int(dni)
        print(f'DNI ingresado: {dni}')
        # Obtenemos todos los datos de la tabla Plan:
        query = Plan.objects.all()
        lista_dni=[]
        for q in query:
            print(q.dni)
            lista_dni.append(q.dni)
        print(lista_dni)
        if dni in lista_dni:
            print('Se encontro dni')
            query = Plan.objects.filter(dni=dni)
            for q in query:
                num_asistencia = q.asistencia
                print(num_asistencia)
                num_asistencia+=1
            # Actualizamos el numero de asistencia de la db sumando uno:
            Plan.objects.filter(dni=dni).update(asistencia = num_asistencia)                
        else:
            print('DNI no encontrado')
            

        # print(request.POST['dni'])
        return redirect("control")
    else:
        return render(request, 'appbase/control.html')