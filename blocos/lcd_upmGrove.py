# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca upm/mraa da intel
Comunica via i2c com o leitor lcd e a luz de fundo

Gustavo Voltani von Atzingen 15/04/2017

Curso IoT 2017 - IFSP Piracicaba
'''

from upm import pyupm_jhd1313m1 as lcd
import time

tela = lcd.Jhd1313m1(0, 0x3E, 0x62)
tela.clear()
tela.setCursor( 0, 0)
tela.write("hello")
tela.setCursor( 1, 0)
tela.write("Segunda linha")

try:
    while 1:
        tela.setColor(255, 0, 0)
        time.sleep(1)
        tela.setColor(0, 0, 255)
        time.sleep(1)

except KeyboardInterrupt:
    print '\nDesligando o Lcd'
    tela.clear()
    tela.displayOff()
    tela.backlightOff()
