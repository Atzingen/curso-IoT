# -*- coding: latin-1 -*-
from Adafruit_IO import Client, Feed
import numpy as np
import time

id_adafruit = 'af4b0d4b19534cbf9b6046955cc6748d'

aio = Client(id_adafruit)
aio.send('teste', 100)
aio.send('potenciometro', 723)

# mostra os nomes dos feeds disponiveis e valores (ultimo)
feeds = aio.feeds()
for f in feeds:
    print 'Feed: {0}'.format(f.name), f.last_value


def send_fake_feed(quantidade, intervalo, media):
    for i in range(quantidade):
        aio.send('teste', np.random.normal(media, 1))
        time.sleep(intervalo)

send_fake_feed(30, 5, 100)
