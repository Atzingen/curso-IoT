import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print 'funcao de coneccao - ' + str(client)

def on_message(client1, userdata, message):
    print "menssagem recebida, topico: {}, valor: {}".format(message.topic, message.payload)

client1 = mqtt.Client()
client1.on_connect= on_connect
client1.on_message=on_message
client1.connect("143.107.188.204")
client1.subscribe("teste")
client1.loop_forever()
