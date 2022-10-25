from re import template
from django.urls import path
from django.views import View

from . import views

# Reset pwd views:
from django.contrib.auth import views as auth_views

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
    path('ctrl_planificacion', views.ctrl_planificacion, name="ctrl_planificacion"),
    # Pwd reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="autenticacion/reinicio_pwd.html"), name="password_reset"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="autenticacion/reinicio_enviado.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="autenticacion/reinicio_completo.html"), name="password_reset_complete"),
]

