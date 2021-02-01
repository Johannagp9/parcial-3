from client.Constantes import APP_NAME
from client.services import generate_get, response_2_dict, generate_post, generate_put


def get_all_imagenes(params,token):
    url = APP_NAME + "/api/imagenes/"
    response = generate_get(url,token,params)
    if response:
        return response_2_dict(response)

def create_imagen(params,token):
    url = APP_NAME + "/api/imagenes/"
    response = generate_post(url,params,token)
    if response:
        return response

def update_imagen(id,params,token):
    url = APP_NAME + "/api/imagenes/"+ id + "/"
    response = generate_put(url,params,token)
    if response:
        return response

def get_imagen(id, token):
    url = APP_NAME + "/api/imagenes/" + id + "/"
    params = {}
    response = generate_get(url, token=token, params=params)
    if response:
        return response_2_dict(response)