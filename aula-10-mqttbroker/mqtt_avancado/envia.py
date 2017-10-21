import mosquitto, sensores
import time

if __name__ == "__main__":
    while 1:
        mosquitto.publica('botao_gal1', sensores.leitura_botao())
        mosquitto.publica('botao_gal1', sensores.leitura_pot())
        time.sleep(0.5)
