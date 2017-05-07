'''
Baseado no exemplo disponibilizado pela biblioteca
Exemplo de manipulação de GPIO usando a bilbioteca wiringx86

Gustavo Voltani von Atzingen 15/04/2017

Curso IoT 2017 - IFSP Piracicaba
'''

import time
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
numero_pino = 13

pinos.pinMode(numero_pino, pinos.OUTPUT)

while(True):
    pinos.digitalWrite(numero_pino, pinos.HIGH)
    time.sleep(1)
    pinos.digitalWrite(numero_pino, pinos.LOW)
    time.sleep(1)
