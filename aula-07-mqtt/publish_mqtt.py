import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('143.107.188.204')

client.publish('teste','ligado')
