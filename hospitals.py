from textwrap import indent
from turtle import circle
from urllib.parse import urlencode
from credentials import api_key
import requests


lat, lan = 25.3498301, 49.5771891
base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params_2 = {
    'key': api_key,
    'location': f'{lat}, {lan}',
    'keyword': 'coffe shope',
    'radius': 50000,
    # 'language': 'ar'
}
params_encode = urlencode(params_2)
url_3 = f'{base_url}?{params_encode}'
# print(url_3)
response = requests.get(url_3)
print(response.json())
