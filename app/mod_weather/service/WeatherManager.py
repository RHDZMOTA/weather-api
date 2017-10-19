import time
import requests
import json

from app import app
from util.distance_operations import harversine
from app.mod_weather.model import RegisterWeather, WeatherQuery, db


class WeatherManager(object):

    def __init__(self):
        self.response = None
        self.epoch_time = int(time.time())

    def get_from_city(self, city):
        query = WeatherQuery.query(
            WeatherQuery.unix_query > self.epoch_time - app.config.get("UPDATE_SECONDS"),
            WeatherQuery.city_name == str(city)).fetch(limit=1)
        if len(query):
            return query[0].jsonify()
        r = requests.get(url=app.config.get("OWM_CITY").format(city=str(city), appid=app.config.get("OWM_KEY")))
        data = r.json()
        return RegisterWeather(data).save().jsonify()

    def get_from_coordinates(self, lat, lng):
        delta_lat, delta_lng = 0.1, 0.1  # this generates a rad of 15 km approx.
        iter_query = WeatherQuery.query(
            WeatherQuery.unix_query > self.epoch_time - app.config.get("UPDATE_SECONDS")).fetch()
        query = [e for e in iter_query if
                 (float(lat) - delta_lat < float(e.lat)) and
                 (float(lat) + delta_lat > float(e.lat)) and
                 (float(lng) - delta_lng < float(e.lng)) and
                 (float(lng) + delta_lng < float(e.lng))]
        if len(query):
            return query[0].jsonify()
        r = requests.get(
            url=app.config.get("OWM_COORDINATES").format(
                lat=str(lat),
                lng=str(lng),
                appid=app.config.get("OWM_KEY")))
        data = r.json()
        return RegisterWeather(data).save().jsonify()

