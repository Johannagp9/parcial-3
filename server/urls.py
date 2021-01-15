from django.urls import path

from server import views

urlpatterns = [
    path('mensajes/', views.MensajeList.as_view()),
    path('mensajes/<str:id>/', views.MensajeDetail.as_view()),
    path('auth/', views.autenticar_usuario),
    path('imagenes/', views.ImagenList.as_view()),
    path('imagenes/<str:id>/', views.ImagenDetail.as_view()),
    path('usuarios/', views.UsuarioList.as_view()),
    path('usuarios/<str:id>/', views.UsuarioDetail.as_view()),

]