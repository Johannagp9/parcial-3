from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from client.mensajes_services import get_mensajes_por_destino, create_mensaje
from client.services import  authenticate_user

INICIAR_SESION_TEMPLATE = "iniciar-sesion.html"
PAGINA_PRINCIPAL_TEMPLATE = "pagina-principal.html"
CREAR_MENSAJE = "crear-mensaje.html"
RESPONDER = "responder.html"


@csrf_exempt
def cerrar_sesion(request):
    request.session['usuario'] = None
    return render(request, INICIAR_SESION_TEMPLATE)


def iniciar_sesion(request):
    return render(request, INICIAR_SESION_TEMPLATE)


@csrf_exempt
def autenticar_usuario(request):
    id_token = request.POST.get('token')
    idinfo = authenticate_user(id_token)
    if idinfo is not None:
        request.session['token'] = idinfo
        return redirect('/cargar-principal')
    else:
        return render(request, INICIAR_SESION_TEMPLATE)


def cargar_principal(request):
    usuario = request.session['token']
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    mensajes = get_mensajes_por_destino({'destino': usuario['email']}, usuario['sub'])

    if mensajes is None:
        mensajes = []

    return render(request, PAGINA_PRINCIPAL_TEMPLATE, {'mensajes': mensajes})


def enviar_respuesta(request):
    usuario = request.session['token']
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    destino = request.POST.get('destino')
    contenido = request.POST.get('contenido')
    response = create_mensaje({'contenido': contenido, 'destino': destino, 'origen': usuario['email']},usuario['sub'])
    if response:
        messages.success(request, "Se ha enviado su mensaje")
    else:
        messages.error(request, "No se ha podido enviar el mensaje")
    return redirect('/cargar-principal')

def guardar_mensaje(request):
    usuario = request.session['token']
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    destino = request.POST.get('destino')
    contenido = request.POST.get('contenido')
    response = create_mensaje({'contenido': contenido, 'destino': destino, 'origen': usuario['email']},usuario['sub'])
    if response:
        messages.success(request, "Se ha enviado su mensaje")
    else:
        messages.error(request, "No se ha podido enviar el mensaje")
    return redirect('/cargar-principal')

def crear_mensaje(request):
    usuario = request.session['token']
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request,CREAR_MENSAJE)


def responder(request, origen ):
    usuario = request.session['token']
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request,RESPONDER, {'origen': origen})
