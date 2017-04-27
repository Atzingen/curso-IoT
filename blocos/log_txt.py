# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca
Exemplo de escrita dos dados da leitura do conversor ADC
em uma arquivo txt

Gustavo Voltani von Atzingen 15/04/2017

Curso IoT 2017 - IFSP Piracicaba
'''
import time
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
pinos.pinMode(14, pinos.ANALOG_INPUT)

while 1:
    with open('dados.txt','a') as f:
        valor = pinos.analogRead(14)
        f.write(str(valor) + '\n')
    print str(valor) + '\n'
    time.sleep(1)
