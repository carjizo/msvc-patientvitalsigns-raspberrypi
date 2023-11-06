# from request_api.api_users import ApisUsers
#
# apis_users = ApisUsers()
#
# data = apis_users.create_user(56,32)
# print(data)

from mqtt.mqtt import MQTT

mqtt = MQTT()
mqtt.get_data()