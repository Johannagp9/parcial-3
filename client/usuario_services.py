from client.Constantes import APP_NAME
from client.services import generate_get, response_2_dict, generate_post


def getUsuarioByToken(token):
    url = APP_NAME + "/api/usuarios/"
    params = {}
    params['google_id'] = token
    response = generate_get(url, token=token, params=params)
    if response:
        return response_2_dict(response)

def create_usuario(usuario, token):
    url = APP_NAME + "/api/usuarios/"
    response = generate_post(url, usuario, token=token)
    return response

