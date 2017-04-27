# -*- coding: latin-1 -*-
'''
Baseado no exemplo disponibilizado pela biblioteca upm/mraa da intel
Para controlar o buzzer.

Gustavo Voltani von Atzingen 15/04/2017

Curso IoT 2017 - IFSP Piracicaba
'''

import time
import mraa
from upm import pyupm_buzzer as upmBuzzer

def desliga_buzzer(pino):
    x = mraa.Gpio(pino)
    x.dir(mraa.DIR_OUT)
    x.write(0)

pino_buzzer = 5
buzzer = upmBuzzer.Buzzer(pino_buzzer)

print upmBuzzer.BUZZER_DO

chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
           upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
           upmBuzzer.BUZZER_SI];

buzzer.setVolume(0.2)

for nota in chords:
    buzzer.playSound(nota, 500000)
    time.sleep(0.1)

desliga_buzzer(pino_buzzer)
