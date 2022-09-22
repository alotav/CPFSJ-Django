from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages # para mostrar mensajes flash
from django.contrib.auth import login, logout, authenticate # para manejar sesiones de usuarios registrados en DB
# Importamos rutina para poder acceder a los datos de la dn a traves de una consulta ORM
from .models import Rutina, Dieta, Usuario
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
    dieta = Dieta.objects.all()
    print(dieta)
    return render(request, 'appbase/dietas.html', {'dieta': dieta})

# def dietas(request):
#     if User.is_authenticated:
#         id_usr = request.user.id
#         print(id_usr)
#         ejemplo2 = Dieta.objects.filter(usr_id=id_usr)
#         print(ejemplo2)
#         return render(request, 'appbase/dietas.html', {'ejemplo2': ejemplo2})

# def dietas(request):
    # if User.is_authenticated:
    #     id_usuario = request.user.id
    #     print(f'User ID: {id_usuario}')
    #     dietas = Dieta.objects.filter(usuario_id = f'{id_usuario}')
    # dieta = 'petete'
    # print(Dieta.objects.all())
    # return render(request, 'appbase/dietas.html', {'dieta': 'Alonso'})

def plan(request):
    return render(request, 'appbase/plan.html')