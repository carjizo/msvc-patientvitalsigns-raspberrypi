# from request_api.api_patient_vital_signs import ApisUsers
# apis_users = ApisUsers()
# data = apis_users.insert_patient_signs(40,80, 1)

from mqtt.mqtt import MQTT

mqtt = MQTT()
mqtt.get_data()