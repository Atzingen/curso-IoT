# -*- coding: latin-1 -*-
import urllib2
import json


response = urllib2.urlopen("http://samples.openweathermap.org/data/2.5/weather?q=London&appid=b1b15e88fa797225412429c1c50c122a1")
page_source = response.read()

dados = json.loads(page_source)
print dados['coord']
print dados['visibility']
print dados['main']['temp_min']
print dados['main']['temp_max']
