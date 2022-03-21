
import requests
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
from credentials import api_key


from geocoding import extract_lat_lng


class Search_Clinet(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    key = api_key

    def __init__(self, key=None, address_or_postal_code=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if key == None:
            raise Exception('api_key is required')
            self.key = api_key
            self.location_query = address_or_postal_code
            if self.location_query != None:
                self.extract_lat_lng()

    def extract_lat_lng(self, location=None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {'address': loc_query, 'key': self.key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        r.json()
        if r.status_code not in range(200, 299):
            return{}
        latlng = {}
        try:
            latlng = r.json()['result'][0]['geometry']['location']
        except:
            pass
        lat, lng = latlng.get('lat'), latlng.get('lng')
        self.lat = lat
        self.lng = lng
        return lat, lng

    def search(self, keyword='coffe shope', radius=5000, location=None):
        lan, lng = self.lan, self.lng
        if location != None:
            lat, lng = self.extract_lat_lng(location=location)
            base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        params_2 = {
            'key': api_key,
            'location': location,
            'keyword': keyword,
            'radius': radius
        }
        params_encode = urlencode(params_2)
        url_search = f'{base_url}?{params_encode}'
        r = requests.get(url_search)
        r.json()
        if r.status_code not in range(200, 299):
            return{}
        return r.json()


client = Search_Clinet(key=api_key, address_or_postal_code=1111)
print(client.lat, client.lng)
