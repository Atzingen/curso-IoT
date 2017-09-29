# -*- coding: latin-1 -*-
import urllib2
import json

'''
Exemplo de criação de uma classe para interação com a api do openweather

Gustavo Voltani von Atzingen 15/04/2017
Updated: 28/09/2017

Curso IoT 2017 - IFSP Piracicaba
'''

class openweather:
    '''
    Uma classe simples que utiliza a api do openweathermap
    para fazer requisições de tempo
    https://openweathermap.org/api
    '''
    def __init__(self, chave, cidade):
        self.cidade = cidade
        self.chave = chave
        self.site = 'http://api.openweathermap.org/data/2.5/weather?id='
        self.update()

    def update(self):
        url = self.site + self.cidade + '&appid=' + self.chave
        resposta = urllib2.urlopen(url)
        dados_resposta = resposta.read()
        dados = json.loads(dados_resposta)
        self.dados = dados

    def temperatura(self):
        return self.dados['main']['temp'] - 273.1

    def pressao(self):
        return self.dados['main']['pressure']

    def descricao(self):
        return self.dados['weather'][0]['description']

    def vento(self):
        return self.dados['wind']['speed'], self.dados['wind']['deg']


if __name__ == '__main__':
    id_piracicaba = '3453643'
    api_key = 'a176d82c6221c89af64489ccb1cf39e8' # troque pela sua api

    piracicaba = openweather(api_key, id_piracicaba)
    print piracicaba.descricao(), 'temperatura: ', piracicaba.temperatura()
