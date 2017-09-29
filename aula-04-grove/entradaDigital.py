# coding: latin1
'''
Baseado no exemplo disponibilizado pela biblioteca
Exemplo de manipulação de GPIO como entrada usando a bilbioteca wiringx86

Gustavo Voltani von Atzingen 15/04/2017
Updated: 28/09/2017

Curso IoT 2017 - IFSP Piracicaba
'''

import time
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
numero_pino = 13

pinos.pinMode(numero_pino, pinos.INPUT)

try:
    while True:
        print pinos.digitalWrite(numero_pino)
        time.sleep(1)

except KeyboardInterrupt:
    print '\nLimpando o uso para fechar o programa'
    pinos.cleanup()
