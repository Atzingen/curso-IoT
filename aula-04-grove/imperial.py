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
buzzer.setVolume(0.1)

n = 6
c = 261*n
d = 294*n
e = 329*n
f = 349*n
g = 391*n
gS =  415*n
a = 440*n
aS =  455*n
b = 466*n
cH =  523*n
cSH =  554*n
dH =  587*n
dSH = 622*n
eH =  659*n
fH =  698*n
fSH = 740*n
gH =  784*n
gSH =  830*n
aH = 880*n

def beep(nota, tempo):
    buzzer.playSound(nota, tempo*1000)

def firstSection():
    beep(a, 500);
    beep(a, 500);
    beep(a, 500);
    beep(f, 350);
    beep(cH, 150);
    beep(a, 500);
    beep(f, 350);
    beep(cH, 150);
    beep(a, 650);

    time.sleep(0.500);

    beep(eH, 500);
    beep(eH, 500);
    beep(eH, 500);
    beep(fH, 350);
    beep(cH, 150);
    beep(gS, 500);
    beep(f, 350);
    beep(cH, 150);
    beep(a, 650);

    time.sleep(0.500);

def secondSection():
    beep(aH, 500);
    beep(a, 300);
    beep(a, 150);
    beep(aH, 500);
    beep(gSH, 325);
    beep(gH, 175);
    beep(fSH, 125);
    beep(fH, 125);
    beep(fSH, 250);

    time.sleep(0.325);

    beep(aS, 250);
    beep(dSH, 500);
    beep(dH, 325);
    beep(cSH, 175);
    beep(cH, 125);
    beep(b, 125);
    beep(cH, 250);

    time.sleep(0.350);


firstSection();

secondSection();

beep(f, 250);
beep(gS, 500);
beep(f, 350);
beep(a, 125);
beep(cH, 500);
beep(a, 375);
beep(cH, 125);
beep(eH, 650);

time.sleep(0.500);

secondSection();

beep(f, 250);
beep(gS, 500);
beep(f, 375);
beep(cH, 125);
beep(a, 500);
beep(f, 375);
beep(cH, 125);
beep(a, 650);

desliga_buzzer(pino_buzzer)
