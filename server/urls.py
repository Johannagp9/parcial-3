from django.urls import path

from server import views

urlpatterns = [
    path('mensajes/', views.MensajeList.as_view()),
    path('mensajes/<str:id>/', views.MensajeDetail.as_view()),
    path('auth/', views.autenticar_usuario),

]