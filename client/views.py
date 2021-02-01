from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from client.imagen_services import get_imagen, update_imagen, get_all_imagenes
from client.mensajes_services import get_mensajes_por_destino, create_mensaje
from client.services import authenticate_user, get_cloudinary_url, paginate
from client.usuario_services import getUsuarioByToken, create_usuario

INICIAR_SESION_TEMPLATE = "iniciar-sesion.html"
PAGINA_PRINCIPAL_TEMPLATE = "panel-imagenes.html"
CREAR_MENSAJE = "crear-mensaje.html"
RESPONDER = "responder.html"
PRINCIPAL_TEMPLATE="principal.html"
SUBIR_IMAGEN_TEMPLATE="subir-imagen.html"
PANEL_IMAGENES_TEMPLATE="panel-imagenes.html"



@csrf_exempt
def cerrar_sesion(request):
    request.session['usuario'] = None
    return render(request, INICIAR_SESION_TEMPLATE)


def iniciar_sesion(request):
    return render(request, INICIAR_SESION_TEMPLATE)


def comprobar_response(request, response):
    if isinstance(response, HttpResponse):
        if response.status_code == 401:
            return render(request, INICIAR_SESION_TEMPLATE)


def comprobar_session(usuario, request):
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)




@csrf_exempt
def autenticar_usuario(request):
    id_token = request.POST.get('token')
    idinfo = authenticate_user(id_token)
    if idinfo is not None:
        usuario = getUsuarioByToken(idinfo['sub'])
        comprobar_response(request, idinfo)
        if usuario is None:
            request.session['usuario'] = idinfo
            usuario = {"google_id": idinfo['sub'], "email": idinfo['email']}
            response = create_usuario(usuario, idinfo['sub'])
            if not response:
                return render(request, PRINCIPAL_TEMPLATE)
        request.session['usuario'] = usuario[0]
        return redirect('/cargar-principal')
    else:
        return render(request, INICIAR_SESION_TEMPLATE)


def cargar_principal(request):
    try:
        usuario = request.session.get('usuario')
        comprobar_session(usuario, request)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)

    mensajes = get_mensajes_por_destino({'destino': usuario['email']}, usuario['sub'])

    if mensajes is None:
        mensajes = []

    return render(request, PAGINA_PRINCIPAL_TEMPLATE, {'mensajes': mensajes})


def enviar_respuesta(request):
    try:
        usuario = request.session.get('usuario')
        comprobar_session(usuario, request)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    destino = request.POST.get('destino')
    contenido = request.POST.get('contenido')
    params = {'contenido': contenido, 'destino': destino, 'origen': usuario['email']}
    foto = get_cloudinary_url(request)
    if foto is not None:
        params['foto'] = foto
    response = create_mensaje(params, usuario['sub'])
    if response:
        messages.success(request, "Se ha enviado su mensaje")
    else:
        messages.error(request, "No se ha podido enviar el mensaje")
    return redirect('/cargar-principal')


def guardar_mensaje(request):
    try:
        usuario = request.session.get('usuario')
        comprobar_session(usuario, request)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    destino = request.POST.get('destino')
    contenido = request.POST.get('contenido')
    params = {'contenido': contenido, 'destino': destino, 'origen': usuario['email']}
    foto = get_cloudinary_url(request)
    if foto is not None:
        params['foto'] = foto
    response = create_mensaje(params, usuario['sub'])
    if response:
        messages.success(request, "Se ha enviado su mensaje")
    else:
        messages.error(request, "No se ha podido enviar el mensaje")
    return redirect('/cargar-principal')


def crear_mensaje(request):
    try:
        usuario = request.session.get('usuario')
        comprobar_session(usuario, request)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request, CREAR_MENSAJE)


def responder(request, origen):
    try:
        usuario = request.session.get('usuario')
        comprobar_session(usuario, request)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request, RESPONDER, {'origen': origen})

def subir_imagen(request):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request, SUBIR_IMAGEN_TEMPLATE, {'usuario': usuario})


def get_imagenes(request):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)


    imagenes = get_all_imagenes({}, usuario['google_id'])
    if imagenes is not None:
        imagenes = paginate(request, imagenes, 9)

    return render(request, PAGINA_PRINCIPAL_TEMPLATE, {'imagenes': imagenes, 'usuario':usuario})

def dar_like(request,id):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)

def update_description(request,id):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    response = update_imagen(id,
                               {"usuario": usuario['id'],
                                "descripcion": request.POST.get("descripcion")}, usuario['google_id'])
    comprobar_response(request, response)


@csrf_exempt
def ajax_filter_imagenes(request):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    descripcion = request.POST.get('descripcion')
    imagenes = get_imagenes({'descripcion':descripcion}, usuario['google_id'])
    comprobar_response(request,imagenes)
    if imagenes is not None:
        imagenes = paginate(request, imagenes, 9)
    return render(request, PAGINA_PRINCIPAL_TEMPLATE, {'imagenes': imagenes, 'usuario': usuario})



def guardar_imagen(request):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    descripcion = request.POST.get('descripcion')
    params = {'descripcion': descripcion, 'usuario': usuario['id']}
    foto = get_cloudinary_url(request)
    if foto is not None:
        params['foto'] = foto
    response = create_mensaje(params, usuario['sub'])
    if response:
        messages.success(request, "Se ha creado su imagen")
    else:
        messages.error(request, "No se ha podido crear su imagen")
    return render(request, SUBIR_IMAGEN_TEMPLATE, {'usuario':usuario})

def editar_descripcion(request,id):
    try:
        usuario = request.session['usuario']
        if usuario is None:
            return render(request, INICIAR_SESION_TEMPLATE)
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    imagen=get_imagen(id,usuario['google_id'])

    return render(request, SUBIR_IMAGEN_TEMPLATE, {'usuario': usuario, 'imagen': imagen })





