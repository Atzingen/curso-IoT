# -*- coding: latin-1 -*-
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
