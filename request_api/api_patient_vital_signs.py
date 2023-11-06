import requests
from jwt.jwt import JWT


class ApisUsers:
    """ APIS del para el microservicio Users """

    def __init__(self):
        pass

    def insert_patient_signs(self, temp, pulso, paciente_id):
        """ API REGISTRAR UN USUARIO """
        # CÓDIGO DE PRUEBA
        jwt = JWT()
        token = jwt.get_token()
        if token != 'NOT_TOKEN':
            url = 'https://msvc-patientvitalsigns-production.up.railway.app/patient-vital-signs/create'
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
