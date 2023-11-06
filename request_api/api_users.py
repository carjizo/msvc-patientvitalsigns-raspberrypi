import requests
from jwt.jwt import JWT


class ApisUsers:
    """ APIS del para el microservicio Users """

    def __init__(self):
        pass

    def get_all_users(self):
        """ API OBTIENE TODOS LOS USUARIOS REGISTRADOS """
        # CÓDIGO DE PRUEBA
        jwt = JWT()
        token = jwt.get_token()
        if token != 'NOT_TOKEN':
            url = 'https://msvc-users-production.up.railway.app/users/getAll'
            bearer_token = token  # Reemplaza con tu token de portador

            headers = {
                "Authorization": f"Bearer {bearer_token}"
            }
            r = requests.get(url, headers=headers)
            data = r.json()  # Si la respuesta es JSON
            return data
        else:
            return 'ERROR'

    def create_user(self, temp, pulso, paciente_id):
        """ API REGISTRAR UN USUARIO """
        # CÓDIGO DE PRUEBA
        jwt = JWT()
        token = jwt.get_token()
        if token != 'NOT_TOKEN':
            url = 'https://msvc-users-production.up.railway.app/users/create'
            bearer_token = token  # Reemplaza con tu token de portador

            headers = {
                "Authorization": f"Bearer {bearer_token}"
            }

            data = {
                "heartRate": pulso,
                "temperature": float(temp),
                "patientId": paciente_id
            }
            r = requests.post(url, json=data, headers=headers)
            return r.status_code
        else:
            return 'ERROR'
