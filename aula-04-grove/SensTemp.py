# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca upm/mraa da intel
para leitura do sensor de temperatura.
O sensor de temperatura é analógico.

Gustavo Voltani von Atzingen 15/04/2017
Updated: 28/09/2017

Curso IoT 2017 - IFSP Piracicaba
'''

import time
from upm import pyupm_temperature as upm

temp = upm.Temperature(0)

for i in range(0, 10):
    celsius = temp.value()
    print "{} graus Celsius".format(celsius)
    time.sleep(1)
