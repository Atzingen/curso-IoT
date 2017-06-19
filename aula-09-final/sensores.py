from wiringx86 import GPIOGalileo as GPIO
from upm import pyupm_jhd1313m1 as lcd

# definicoes do lcd
tela = lcd.Jhd1313m1(0, 0x3E, 0x62)
tela.clear()
tela.setCursor( 0, 0)

# pinos fisicos conectados ao shield grove
pino_pot = 14
pino_botao = 5
pino_rele = 13

# cria o objeto para leitura do potenciometro
potenciometro = GPIO(debug=False)
potenciometro.pinMode(pino_pot, potenciometro.ANALOG_INPUT)

# cria o objeto para leitura do rele
rele = GPIO(debug=False)
rele.pinMode(pino_rele, rele.OUTPUT)

# cria o objeto para leitura do botao
botao = GPIO(debug=False)
botao.pinMode(pino_botao, botao.INPUT)

def leitura_pot():
    try:
        return potenciometro.analogRead(pino_pot)
    except Exception as e:
        print 'erro leitura_pot', e
        return None

def leitura_botao():
    try:
        return botao.digitalRead(pino_botao)
    except Exception as e:
        print 'erro leitura_pot', e
        return None

def altera_rele(estado):
    try:
        if estado == True:
            rele.digitalWrite(pino_rele, rele.HIGH)
        else:
            rele.digitalWrite(pino_rele, rele.LOW)
    except Exception as e:
        print 'erro altera_rele', e

def escreve_lcd(texto):
    try:
        tela.clear()
        tela.setCursor( 1, 0)
        tela.write(str(texto))
    except Exception as e:
        print 'erro escreve_lcd', e
