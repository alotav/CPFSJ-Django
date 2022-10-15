from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('acceder', views.acceder, name='acceder'),
    path('home.html', views.home, name='home'),
    path('rutinas.html', views.rutinas, name='rutinas'),
    path('dietas.html', views.dietas, name='dietas'),
    path('plan.html', views.plan, name='plan'),
    path('registro.html', views.VistaRegistro.as_view(), name="registro"),
    path('salir', views.cerrar_sesion, name="salir"),
    path('control', views.control, name="control"),
    path('planificacion', views.tipo_rutina, name="planificacion"),
    path('planificacion_semanal', views.rutina_semanal, name="planificacion_semanal"),
    path('ctrl_planificacion', views.ctrl_planificacion, name="ctrl_planificacion")
]

