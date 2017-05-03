# -*- coding: latin-1 -*-
import pyowm

owm = pyowm.OWM('a176d82c6221c89af64489ccb1cf39e8')

################ Previsao do tempo ############################
forecast = owm.daily_forecast("Brasilia,BR")
tomorrow = pyowm.timeutils.tomorrow()
print forecast.will_be_sunny_at(tomorrow)

################  Tempo agora  ##################
observation = owm.weather_at_place('Piracicaba,BR')
w = observation.get_weather()

# w.get_wind()  -> {'speed': 4.6, 'deg': 330}
#  w.get_temperature('celsius') -> {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print 'vento: velocidade = {}, direcao = {}'.format(w.get_wind()['speed'], w.get_wind()['deg'] )
print 'umidade do ar: ', w.get_humidity()
print 'temperatura: ', w.get_temperature('celsius')['temp_max']
