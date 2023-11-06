import json

import paho.mqtt.client as mqtt
import mqtt.config as cfg
from request_api.api_users import ApisUsers


class MQTT:

    def __int__(self):
        self.mqtt_topic = cfg.TOPIC
        self.mqtt_port = cfg.PORT
        self.mqtt_broker = cfg.BROKER

    def on_connect(self, client, userdata, flags, rc):
        """ CONECTANDO AL BROKER Y VERIFICA """
        if rc == 0:
            print("Conexión exitosa al broker MQTT")
            client.subscribe(self.mqtt_topic)
        else:
            print(f"Error en la conexión al broker MQTT con código de resultado {rc}")

    def on_message(self, client, userdata, msg):
        """ OBTIENE EL MENSAJE """
        try:
            payload = msg.payload.decode("utf-8")
            data = json.loads(payload)
            pulso = data.get("pulso")
            temperatura = data.get("temperatura")
            paciente_id = data.get("paciente_id")

            if pulso is not None and temperatura is not None and paciente_id is not None:
                print(f"Pulso: {pulso} lpm, Temperatura: {temperatura}°C")
                # USAR LA API PARA REGISTRAR LOS PULSOS
                create_users = ApisUsers()
                create_users.create_user(temperatura, pulso, paciente_id)

        except Exception as e:
            print("Error al procesar el mensaje MQTT:", str(e))

    def get_data(self):
        """ VERIFICA EL ESTADO DE LA CONEXIÓN Y OBTIENE LA DATA """
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        try:
            client.connect(self.mqtt_broker, self.mqtt_port, 60)
            client.loop_forever()
        except Exception as e:
            print("Error en la conexión MQTT:", str(e))
