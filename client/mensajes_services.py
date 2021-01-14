from client.Constantes import APP_NAME
from client.services import generate_get, response_2_dict, generate_post


def get_mensajes_por_destino(params,token):
    url = APP_NAME + "api/mensajes/"
    response = generate_get(url,token,params)
    if response:
        return response_2_dict(response)

def create_mensaje(params,token):
    url = APP_NAME + "api/mensajes/"
    response = generate_post(url,params,token)
    if response:
        return response