# from contextvars import Context
# from dataclasses import asdict
from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime

from django.contrib import messages # para mostrar mensajes flash

from django.contrib.auth import login, logout, authenticate # para manejar sesiones de usuarios registrados en DB
# Importamos rutina para poder acceder a los datos de la dn a traves de una consulta ORM
from .models import Rutina, Dieta, Plan,Usuario, RutinaSemanal
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
            messages.error(request, 'Los datos son incorrectos!')
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
                messages.error(request, "Los datos son incorrectos!")
        else:
            messages.error(request, "Los datos son incorrectos!")
    # llamamos al formulario:
    form = AuthenticationForm()
    return render(request, "appbase/index.html", {"form": form})



def index(request):
    return render(request,'appbase/index.html')



def ctrl_planificacion(request):
        # if User.is_authenticated:
        # Verificamos si el usuario es admin:
            usr_cercavto = {}
            if User.is_staff:
                datos_rsemanal = RutinaSemanal.objects.all()
                datos_users = User.objects.all()
                for datos in datos_rsemanal:
                    # si estan vencidos obtenemos los usuarios:
                    if datos.cerca_vto == True:
                        print(f'ID: {datos.usuario_id}')
                        id_usuario = datos.usuario_id
                        for user in datos_users:
                            if user.id == id_usuario:
                                # Pasamos por dict los vencimientos al view:
                                usr_cercavto.update({user.username:user.username})
                                print(usr_cercavto)
                                print(f'Rutina por vencer. Usuario: {user.username}\n')
                                
            return render(request,'appbase/ctrl_planificacion.html', {'usr_vto': usr_cercavto})

                



def home(request):
    # if User.is_authenticated:
    #     # Verificamos si el usuario es admin:
    #     if User.is_staff:
    #         datos_rsemanal = RutinaSemanal.objects.all()
    #         datos_users = User.objects.all()
    #         for datos in datos_rsemanal:
    #             # si estan vencidos obtenemos los usuarios:
    #             if datos.cerca_vto == True:
    #                 print(f'{datos.usuario_id}')
    #                 id_usuario = datos.usuario_id
    #                 for user in datos_users:
    #                     if user.id == id_usuario:
    #                         print(f'Rutina vencida para usuario {user.username}')

        id_usuario = request.user.id
        print(f'User ID: {id_usuario}')
        consulta_planificacion = RutinaSemanal.objects.filter(usuario_id = id_usuario)
        for consulta in reversed(consulta_planificacion):
            f_planificacion = consulta.created
            print(f_planificacion)
            
            # CALCULAMOS LAFECHA DE VTO DEL PLAN:
            
            if consulta.semana8:
                delta = 56
            elif consulta.semana7:
                delta = 49
            elif consulta.semana6:
                delta = 42
            elif consulta.semana5:
                delta = 35
            elif consulta.semana4:
                delta = 28
            elif consulta.semana3:
                delta = 21
            elif consulta.semana2:
                delta = 14
            elif consulta.semana1:
                delta = 7


            fecha_vto = f_planificacion + timedelta(days = delta)
            print(fecha_vto)
            RutinaSemanal.objects.filter(usuario_id = id_usuario).update(f_vencimiento = fecha_vto)
            
            # ENVIAMOS MENSAJE DE ALERTA 5 DIAS ANTES DEL VENCIMIENTO:
            dia_actual = datetime.now()
            print(dia_actual)

            # Quitamos la zona horaria que molesta para obtener la diferencia de dias
            # Tambien quitamos la hora al dia_actual, y obtenemos solo la fecha de ambos.
            fecha_vto = str(fecha_vto)
            fecha_vto_limpia = fecha_vto.split(' ')
            fecha_vto_limpia = fecha_vto_limpia[0]
            fecha_vto_limpia = fecha_vto_limpia.split('-')
            anio = int(fecha_vto_limpia[0])
            mes = int(fecha_vto_limpia[1])
            dia = int(fecha_vto_limpia[2])

            fecha_vto_limpia = date(anio,mes,dia)
            print (f'Fecha_vto limpia: {fecha_vto_limpia}')
            print (f'Fecha_vto limpia: {type(fecha_vto_limpia)}')


            dia_actual = str(dia_actual)
            dia_actual_limpio = dia_actual.split(' ')
            dia_actual_limpio = dia_actual_limpio[0]
            dia_actual_limpio = dia_actual_limpio.split('-')
            anio = int(dia_actual_limpio[0])
            mes = int(dia_actual_limpio[1])
            dia = int(dia_actual_limpio[2])
            
            dia_actual_limpio = date(anio,mes,dia)
            print (f'Fecha_actual limpia: {dia_actual_limpio}')
            print (f'Fecha_actual limpia: {type(dia_actual_limpio)}')

            diferencia = dia_actual_limpio - fecha_vto_limpia
            print(diferencia)
            # Pasamos los dias a entero:
            diferencia = str(diferencia)
            diferencia = diferencia.split(' ')
            diferencia = int(diferencia[0])
            print(diferencia)

            # AGREGAMOS MENSAJES PARA FECHA CERCANA AL VENCIMIENTO Y PARA PLANIFICACION VENCIDA:

            if diferencia > -5 and diferencia < 0:
                messages.warning(request, 'Tu planificacion esta por vencer')
                RutinaSemanal.objects.filter(usuario_id = id_usuario).update(cerca_vto = True)
            elif diferencia >= 0:
                messages.warning(request, 'Tu planificacion esta vendica')

            # Si el usr es admin, recorremos todas las rutinas cerca del vto:
            if User.is_staff:
                datos_rsemanal = RutinaSemanal.objects.all()                        
                if consulta.cerca_vto == True:
                    print(consulta)
                    messages.warning(request, 'Hay planificaciones cerca de vencimiento!')
                    break

        return render(request,'appbase/home.html')






def rutinas(request):
    if User.is_authenticated:
        # Obtenemos en la variable el id de usuario para luego filtrarlo:
        id_usuario = request.user.id
        # ayuda para saber id
        print(f'User ID: {id_usuario}')
        # filtramos por medio del id. La variable usuario_id corresponde a la relacion de la db creada por el model:
        rutinas = Rutina.objects.filter(usuario_id = f'{id_usuario}')
        # VERIFICAMOS SI EL QUERYSET DEVUELVE DATOS EN LA BD:
        print(len(rutinas.values_list()))
        if (len(rutinas.values_list())) == 0:
            messages.error(request, "Aun no se cargaron los datos de tu rutina.")
            return redirect('home')
        else:
            return render(request, 'appbase/rutinas.html', {'rutinas':rutinas})




def tipo_rutina(request):
    return render(request, 'appbase/tipo_rutina.html')



def rutina_semanal(request):
    if User.is_authenticated:
        id_usuario = request.user.id
        # Imprimimos por consola id:
        print(f'User ID: {id_usuario}')
        # filtramos por medio del id. La variable usuario_id corresponde a la relacion de la db creada por el model:
        rutina_semanal = RutinaSemanal.objects.filter(usuario_id = f'{id_usuario}')
        # VERIFICAMOS SI EL QUERYSET DEVUELVE DATOS EN LA BD:
        print(len(rutina_semanal.values_list()))
        if (len(rutina_semanal.values_list())) == 0:
            messages.error(request, "Aun no se cargaron los datos de tu rutina.")
            return redirect('planificacion')
        else:
            return render(request, 'appbase/rutina_semanal.html', {'rutina_semanal':rutina_semanal})


def dietas(request):
    if User.is_authenticated:
        id_usr = request.user.id
        dieta = Dieta.objects.filter(usr_id = id_usr )
        print(len(dieta.values_list()))
        if (len(dieta.values_list())) == 0:
            messages.error(request, "Aun no se cargaron los datos de tu dieta.")
            return redirect('home')
        else:
            return render(request, 'appbase/dietas.html', {'dieta': dieta})

def plan(request):
    # Obtenemos el id para actualizar los registros:
    if User.is_authenticated:  
        id_usr = request.user.id
        print(f'ID Usuario {id_usr}')
        
        # OBTENEMOS LOS REGISTROS PARA ESE USUARIO: SI NO TIENE REGISTROS DARA ERROR:
        # EN CADA CONSULTA A LA DB AGREGAR TRY EXCEPT, MOSTRAR PLANTILLA VACIA, E INFORMAR POR POPUP
        try:
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
                    print(vencido)
                else:
                    vencido = 'No'
                    print(vencido)

                # PLAN ELEGIDO:
                if ocho == True:
                    ocho = 8
                    plan = 'x 8'
                    restantes = ocho - asistencias
                    print(restantes)
                    if restantes < 0:
                        restantes = 0
                        print(restantes)
                    
                    
                elif doce == True:
                    doce = 12
                    plan = 'x 12'
                    restantes = doce - asistencias
                    print(restantes)
                    if restantes < 0:
                        restantes = 0
                        print(restantes)
                elif full == True:
                    restantes = 'Full'
                    plan = 'Full'
                    print(restantes)

            return render(request, 'appbase/plan.html',{'f_pago': planes,'pago':pago,'vencido':vencido,'fecha_venc': vencimiento,'restantes': restantes,'plan': plan,})
        
        except UnboundLocalError:
            messages.add_message(request, messages.ERROR, 'Aun no se cargaron los datos de tu plan.')
            return redirect("home")

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
            messages.add_message(request=request, level=messages.SUCCESS, message = 'Usuario Ingresado!')
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