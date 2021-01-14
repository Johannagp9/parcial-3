from django.urls import path

from client import views

urlpatterns = [
    path('', views.iniciar_sesion),
    path('autenticar/', views.autenticar_usuario, name='autenticar'),
    path('cerrar-sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('cargar-principal/', views.cargar_principal, name='cargar_principal'),
    path('enviar-respuesta/', views.enviar_respuesta, name="enviar_respuesta"),
    path('guardar-mensaje/', views.guardar_mensaje, name="guardar_mensaje"),
    path('crear-mensaje/', views.crear_mensaje, name="crear_mensaje"),
    path('responder/<str:origen>', views.responder, name="responder"),
]