from django.urls import path

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
]

