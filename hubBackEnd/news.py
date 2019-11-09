from newsapi import NewsApiClient
import json, warnings
import geocoder
from geopy.geocoders import Nominatim

warnings.filterwarnings("ignore", category=DeprecationWarning)

g = geocoder.ip('me')
geolocator = Nominatim()

location = geolocator.reverse("{}, {}".format(g.latlng[0],g.latlng[1]))
arr = location.address.split(',')
city = arr[3]

# Init
newsapi = NewsApiClient(api_key='0ec66f777ef14dca99b2a1ad455c0282')

# /v2/top-headlines
local_headlines = newsapi.get_everything(q=city,page_size=5)
national_headlines = newsapi.get_top_headlines(language='en',country='us')
#Local News
x = local_headlines
y = national_headlines

with open('main.json', 'r') as t:
    json_data = json.load(t)
    #json_data['localNews'][0]['1']['title']
    
    #title
    json_data['localNews'][0]['1']['title'] = x['articles'][0]['title']
    json_data['localNews'][0]['2']['title'] = x['articles'][1]['title']
    json_data['localNews'][0]['3']['title'] = x['articles'][2]['title']
    json_data['localNews'][0]['4']['title'] = x['articles'][3]['title']
    json_data['localNews'][0]['5']['title'] = x['articles'][4]['title']
    
    #description
    json_data['localNews'][0]['1']['description'] = x['articles'][0]['description']
    json_data['localNews'][0]['2']['description'] = x['articles'][1]['description']
    json_data['localNews'][0]['3']['description'] = x['articles'][2]['description']
    json_data['localNews'][0]['4']['description'] = x['articles'][3]['description']
    json_data['localNews'][0]['5']['description'] = x['articles'][4]['description']
    
    #url
    json_data['localNews'][0]['1']['url'] = x['articles'][0]['url']
    json_data['localNews'][0]['2']['url'] = x['articles'][1]['url']
    json_data['localNews'][0]['3']['url'] = x['articles'][2]['url']
    json_data['localNews'][0]['4']['url'] = x['articles'][3]['url']
    json_data['localNews'][0]['5']['url'] = x['articles'][4]['url']
    
    #NATIONAL NEWS
    
    #title
    json_data['nationalNews'][0]['1']['title'] = y['articles'][0]['title']
    json_data['nationalNews'][0]['2']['title'] = y['articles'][1]['title']
    json_data['nationalNews'][0]['3']['title'] = y['articles'][2]['title']
    json_data['nationalNews'][0]['4']['title'] = y['articles'][3]['title']
    json_data['nationalNews'][0]['5']['title'] = y['articles'][4]['title']
    
    #description
    json_data['nationalNews'][0]['1']['description'] = y['articles'][0]['description']
    json_data['nationalNews'][0]['2']['description'] = y['articles'][1]['description']
    json_data['nationalNews'][0]['3']['description'] = y['articles'][2]['description']
    json_data['nationalNews'][0]['4']['description'] = y['articles'][3]['description']
    json_data['nationalNews'][0]['5']['description'] = y['articles'][4]['description']
    
    #url
    json_data['nationalNews'][0]['1']['url'] = y['articles'][0]['url']
    json_data['nationalNews'][0]['2']['url'] = y['articles'][1]['url']
    json_data['nationalNews'][0]['3']['url'] = y['articles'][2]['url']
    json_data['nationalNews'][0]['4']['url'] = y['articles'][3]['url']
    json_data['nationalNews'][0]['5']['url'] = y['articles'][4]['url']
    
with open('main.json', 'w') as f:
    f.write(json.dumps(json_data))
    f.close()