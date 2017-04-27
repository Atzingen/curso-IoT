# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca
Exemplo de escrita dos dados da leitura do conversor ADC

Gustavo Voltani von Atzingen 15/04/2017

Curso IoT 2017 - IFSP Piracicaba
'''
import time
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
pinos.pinMode(14, pinos.ANALOG_INPUT)

while 1:
    valor = pinos.analogRead(14)
    print valor
    time.sleep(1)
