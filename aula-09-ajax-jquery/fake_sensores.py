import time
import random

def leitura_temperatura():
    return 27 + 2*random.random()

def leitura_pot():
    return random.randint(0, 1023)

def liga_rele():
    print "led ligado"

def desliga_rele():
    print "led desligado"

def move_servo(posicao):
    print "servo posicao = " + str(posicao)

def escreve_lcd(texto_linha1, texto_linha2):
    print 'lcd linha1: ' + texto_linha1
    print 'lcd linha2: ' + texto_linha2
