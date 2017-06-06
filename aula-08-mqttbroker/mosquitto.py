import paho.mqtt.client as mqtt
import thread
import time
import sensores

client = mqtt.Client()
ip_broker = "143.107.188.204"

def on_connect(client, userdata, flags, rc):
    print 'funcao de coneccao - ' + str(client)

def on_message(client, userdata, message):
    print "menssagem recebida, topico: {}, valor: {}".format(message.topic, message.payload)
    #trata_msg(message)

def publica(topico, valor):
    try:
        client.connect('143.107.188.204')
        client.publish(topico,valor)
    except Exception as e:
        print 'erro publica', e

def run_client(client, ip_broker, topicos):
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(ip_broker)
    for topico in topicos:
        client.subscribe(topico)
    client.loop_forever()

if __name__ == "__main__":
    topicos = ['botao_gal1', 'botao_gal2', 'botao_gal3', 'botao_geral',
               'pot_gal1', 'pot_gal2', 'pot_gal3', 'pot_geral']
    run_client(client, ip_broker, topicos)
    #thread.start_new_thread(run_client,(client, ip_broker, topicos))
    # while 1:
    #     publica('botao_gal1', sensores.leitura_botao())
    #     publica('botao_gal1', sensores.leitura_pot())
    #     time.sleep(0.5)
