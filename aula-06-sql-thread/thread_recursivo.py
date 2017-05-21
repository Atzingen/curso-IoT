from __future__ import division
import threading
import time

class threadLed(threading.Thread):
    ''' Exemplo de imprementacao de uma classe para uso concorrente '''
    def __init__(self, nome, frequencia):
        threading.Thread.__init__(self)
        self.nome = nome
        self.frequencia = frequencia
        self.executando = True

    def run(self):
        if self.executando:
            print 'piscaLed', self.name
            threading.Timer(1/self.run,piscaLed)

    def parar(self):
        print 'parando thread', self.nome
        self.executando = False

led13 = threadLed('led13', 1)
led07 = threadLed('led07', 1.7)

led13.start()
led07.start()
time.sleep(10)
led13.parar()
time.sleep(10)
led07.parar()
