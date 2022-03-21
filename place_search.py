
from urllib.parse import urlencode
from credentials import api_key
import requests


lat, lng = 25.3498301, 49.5771891
place_endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
params = {'key': api_key, 'input': 'Hospitals',
          'inputtype': 'textquery',
          'Basic fields': 'formatted_address,geometry,name',
          'contact fields': 'formatted_phone_number, international_phone_number, opening_hours, website'}
locationbias = f'point : {lat}, {lng}'
use_cirular = False
if use_cirular:
    radius = 100000
    locationbias = f'circle:{radius}@{lat},{lng}'
params['locationbias'] = locationbias
url_params = urlencode(params)
url = f"{place_endpoint}?{url_params}"
r = requests.get(url)
print(r.status_code)
print(r.json())
