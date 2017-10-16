import json

from openweather import openopenweather
from sensores import *

with open('config.txt') as json_data:
    config = json.load(json_data)

api_key = config['api_key']
