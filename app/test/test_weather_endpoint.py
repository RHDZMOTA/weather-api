import requests
import json

from util.distance_operations import harversine

URL_LOCAL = "http://localhost:8080/weather"
URL_PRODUCTION = "https://crabi-weather-api.appspot.com/weather"
COORDS_ENDPOINT = '/coordinates'
CITY_ENDPOINT = "/city/{city}"


class CoordinatesTester:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def request(self, base_url):
        r = requests.get(
            url=base_url + COORDS_ENDPOINT + "?lat={}&lng={}".format(self.lat, self.lng))
        try:
            return r.json()
        except Exception as e:
            return {"error": str(e), "response": r, "text": r.text}

    def request_local(self):
        return self.request(URL_LOCAL)

    def request_production(self):
        return self.request(URL_PRODUCTION)


class CityTester:
    def __init__(self, city):
        self.city = city

    def request(self, base_url):
        r = requests.get(
            url=base_url + CITY_ENDPOINT.format(city=self.city))
        try:
            return r.json()
        except Exception as e:
            return {"error": str(e), "response": r, "text": r.text}

    def request_local(self):
        return self.request(URL_LOCAL)

    def request_production(self):
        return self.request(URL_PRODUCTION)



# TEST CRABI LOCATION
crab_lat, crab_lng = "20.71212", "-103.40991"

dlat = -0.1
dlon = -0.1
harversine([20.71212, -103.40991], [20.71212 + dlat, -103.40991 + dlon])


coord_response_local = CoordinatesTester(crab_lat, crab_lng).request_local()
coord_response_local

coord_response_production = CoordinatesTester(crab_lat, crab_lng).request_production()
coord_response_production

# TEST CRABI CITY
crab_city = "Zapopan"

city_response_local = CityTester(crab_city).request_local()
city_response_local

city_response_production = CityTester(crab_city).request_production()
city_response_production