from django.urls import path

from client import views

urlpatterns = [
    path('', views.iniciar_sesion),
    path('autenticar/', views.autenticar_usuario, name='autenticar'),
    path('cerrar-sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('cargar-principal/', views.get_imagenes, name='cargar_principal'),
    path('enviar-respuesta/', views.enviar_respuesta, name="enviar_respuesta"),
    path('guardar-mensaje/', views.guardar_mensaje, name="guardar_mensaje"),
    path('crear-mensaje/', views.crear_mensaje, name="crear_mensaje"),
    path('responder/<str:origen>', views.responder, name="responder"),
    path('ajax-imagen/',views.ajax_filter_imagenes,name='ajax_filtrar_imagen'),
    path('subir-imagen/',views.subir_imagen,name='subir_imagen'),
    path('actualizar-imagen/<str:id>',views.update_description,name='editar_descripcion'),
    path('dar-like/<str:id>',views.dar_like,name='nuevo_like')
]