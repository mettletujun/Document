from os import path
import csv
from datetime import datetime
import json
import time
import paho.mqtt.client as mqtt

id = '<ID>'
client_name = id + "temperature_sensor_server"

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

temperature_record_file = 'temperature.csv'
fieldnames = ['date', 'temperature']

if not path.exists(temperature_record_file):
    with open(temperature_record_file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    with open(temperature_record_file, mode='a') as temperature_file:
        temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
        temperature_writer.writerow({'date' : datetime.now().astimezone.replace(microsecond=0).isoformat(), 'temperature': payload['temperature']})


mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)