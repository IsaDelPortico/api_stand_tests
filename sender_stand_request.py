import configuration
import requests
import data

def post_new_user(body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                        json=body,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Funcion para crear un nuevo kit de producto
def post_new_client_kit(bodykit, token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_URL,
                         json=bodykit,
                         headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer "+ str(token) }
                         )