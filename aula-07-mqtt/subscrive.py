# -*- coding: latin-1 -*-
import sys
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY      = 'af4b0d4b19534cbf9b6046955cfdsfd'
ADAFRUIT_IO_USERNAME = 'SeuUsername'

FEED_ID = 'teste'


def connected(client):
    # Funcao que sera chamada quando se conectar ao broker
    client.subscribe(FEED_ID)
    print 'Conectado ao Adafruit IO!  Aguardando mudancas em {0}.'.format(FEED_ID)

def disconnected(client):
    print 'Desconectado de Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # A função mensagem é chamada quando um feed é atualizado
    print 'Feed {0} recebido. Valor: {1}'.format(feed_id, payload)


# Cria uma instância do cliente MQTT do servidor adafruit.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Conecta os eventos as funções declaradas acima
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()
client.loop_blocking()
