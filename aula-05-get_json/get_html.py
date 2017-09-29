# -*- coding: latin-1 -*-
'''
Exemplo de comunicação web utilizando TCP/IP.
Pedido 'get' com a biblioteca request e tratamento do conteúdo
(webscrap) com auxílio da biblioteca BeautifulSoup

Gustavo Voltani von Atzingen 15/04/2017
Updated: 28/09/2017

Curso IoT 2017 - IFSP Piracicaba
'''

import urllib2
import requests
from bs4 import BeautifulSoup

url = "http://prc.ifsp.edu.br/index.php/editais"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

print soup.prettify('latin-1')

for link in soup.find_all('a'):
    if 'resultado' in link.get('href'):
        print link.get('href')
