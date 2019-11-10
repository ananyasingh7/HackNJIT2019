import json, requests
import geocoder
from geopy.geocoders import Nominatim
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


g = geocoder.ip('me')
geolocator = Nominatim()

location = geolocator.reverse("{}, {}".format(g.latlng[0],g.latlng[1]))
arr = location.address.split(',')
city = arr[3]

work = "Union+Beach+NJ"
workString = "Union Beach, NJ"
home = "Highland+Park+NJ"
homeString = "Highland Park, NJ"


base_url = "https://maps.googleapis.com/maps/api/directions/json?"
origin = city
destination1 = work
destination2 = home
api_key = "AIzaSyDRp4m_dZVS6eGY1bd2IyNJJ738YOEc3Qc"

url1 = base_url+"origin="+origin+"&"+"destination="+destination1+"&"+"key="+api_key
url2 = base_url+"origin="+origin+"&"+"destination="+destination2+"&"+"key="+api_key
response = requests.get(url1)
response2 = requests.get(url2)
x = response.json()
y = response2.json()
duration1 = x["routes"][0]["legs"][0]["duration"]['text']
distance1 = x["routes"][0]["legs"][0]["distance"]['text']
duration2 = y["routes"][0]["legs"][0]["duration"]['text']
distance2 = y["routes"][0]["legs"][0]["distance"]['text']

with open('main.json', 'r') as t:
    json_data = json.load(t)
    json_data['maps'][0]['work']['origin'] = city
    json_data['maps'][0]['work']['destination'] = destination1
    json_data['maps'][0]['work']['distance'] = distance1
    json_data['maps'][0]['work']['time'] = duration1
    
    json_data['maps'][0]['home']['origin'] = city
    json_data['maps'][0]['home']['destination'] = destination2
    json_data['maps'][0]['home']['distance'] = distance2
    json_data['maps'][0]['home']['time'] = duration2
    
with open('main.json', 'w') as f:
    f.write(json.dumps(json_data))
    f.close()