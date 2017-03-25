# -*- coding: utf-8 -*-

import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

latitude = -37.8420
longitude = 144.8840


#forecast = forecastio.load_forecast(api_key, lat, lng).currently()

#print("{} and {}°".format(forecast.summary, forecast.temperature))

def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address, timeout=10)
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	return"{} and {}° at {}".format(forecast.summary, forecast.temperature, address)

