from urllib.parse import urlencode
from credentials import api_key
import requests

# data_type = 'json'
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params =  {'address' : 'Sudan Khartoum Nourth, Alkadaro','key' : api_key}
# url_params = urlencode(params)
# url = f"{endpoint}?{url_params}"
# print(url)


def extract_lat_lng(address_or_postalcode, data_type="json"):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {'address': address_or_postalcode, 'key': api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return{}
    return r.json()["results"][0]['geometry']['location']


print(extract_lat_lng('Munifah, Al Hofuf 36441'))
