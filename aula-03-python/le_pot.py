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
