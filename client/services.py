import json

import cloudinary.uploader
import requests
from django.http import HttpResponse

from client.Constantes import APP_NAME

headers = {'content_type': 'application/json'}


def generate_get(url, token, params):
    try:
        headers['Authorization'] = token
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    response = requests.get(url, params=params, headers=headers)
    print(response)
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()
    elif response.status_code == 401:
        return response


def response_2_dict(response):
    # No hago get de nada de la response porque lo quiero todo
    json_response = json.dumps(response)
    result = json.loads(json_response)  # String to list
    print(result)
    return result


def generate_post(url, datos, token):
    try:
        headers['Authorization'] = token
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    response = requests.post(url, json=datos, headers=headers)
    return response


def generate_delete(url, token):
    try:
        headers['Authorization'] = token;
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    response = requests.delete(url)
    return response


def generate_put(url, datos, token):
    try:
        headers['Authorization'] = token
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    response = requests.put(url, json=datos, headers=headers)
    return response


def authenticate_user(id_token):
    # Llamo a la API.
    url = APP_NAME + "api/auth/"
    params = {'token': id_token}
    header = {'content_type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, params, headers=header)
    if response:
        return response_2_dict(response.json())
    return None


def get_cloudinary_url(request):
    if len(request.FILES) > 0:
        file = request.FILES['foto']
        print(file)
        try:
            result = cloudinary.uploader.upload(file, transformation=[
                {'width': 500, 'crop': 'scale', }])
            foto_url = result["url"]
            return foto_url
        except:
            print("No se ha podido subir la imagen")
    return None
