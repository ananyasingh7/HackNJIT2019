import warnings
import requests, json
import geocoder
from geopy.geocoders import Nominatim
import pytemperature
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

g = geocoder.ip('me')
geolocator = Nominatim()

location = geolocator.reverse("{}, {}".format(g.latlng[0],g.latlng[1]))
arr = location.address.split(',')
city = arr[3]

api_key="b1e5608a357abaaa13b687491225b6c4"
base_url="http://api.openweathermap.org/data/2.5/weather?"

complete_url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url) 
x = response.json()


if x["cod"] != "404":
    weather_main = x['weather'][0]['main']
    weather_description = x['weather'][0]['description']
    weather_main_temp = x['main']['temp']
    weather_temp_min = x['main']['temp_min']
    weather_temp_max = x['main']['temp_max']
    weather_wind = x['wind']['speed']
    weather_sunrise = x['sys']['sunrise']
    weather_sunset = x['sys']['sunset']
    
    sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(weather_sunrise))
    sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(weather_sunset))
    
    weather_main_temp=pytemperature.k2f(weather_main_temp)
    weather_temp_min=pytemperature.k2f(weather_temp_min)
    weather_temp_max=pytemperature.k2f(weather_temp_max)
else: 
    print(" City Not Found ") 

with open('main.json', 'r') as t:
    json_data = json.load(t)
    json_data['weather'][0]['description'] = weather_description
    json_data['weather'][0]['temperature'] = weather_main_temp
    json_data['weather'][0]['minTemperature'] = weather_temp_min
    json_data['weather'][0]['maxTemperature'] = weather_temp_max
    json_data['weather'][0]['wind'] = weather_wind
    json_data['weather'][0]['sunrise'] = sunrise
    json_data['weather'][0]['sunset'] = sunset
    
with open('main.json', 'w') as f:
    f.write(json.dumps(json_data))
    f.close()

