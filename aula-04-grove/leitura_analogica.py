# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca wiringx86 para GalileoBoard
Exemplo de leitura do conversor ADC ("leitura analógica")

Gustavo Voltani von Atzingen 15/04/2017
Updated: 28/09/2017

Curso IoT 2017 - IFSP Piracicaba
'''
import time
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)               # Degub False para evitar info no terminal
pinos.pinMode(14, pinos.ANALOG_INPUT)   # A0 = 14, A1 = 15, ...

while 1:
    valor = pinos.analogRead(14)
    print valor
    time.sleep(1)
