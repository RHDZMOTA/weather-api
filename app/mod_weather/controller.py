import json

from flask import Blueprint, request, render_template, flash, jsonify, Response
from app import app

from app.mod_weather.service import WeatherManager

mod_weather = Blueprint('weather', __name__, url_prefix='/weather')


@mod_weather.route('/', methods=['GET'])
def weather_hello():
    return "Weather API"


@mod_weather.route('/coordinates', methods=['GET', 'POST'])
def get_weather_by_coordinates():
    lat = request.args.get("lat") if request.method == "GET" else request.get_json().get("lat")
    lng = request.args.get("lng") if request.method == "GET" else request.get_json().get("lng")
    return jsonify(eval(WeatherManager().get_from_coordinates(lat, lng))) #Response(WeatherManager().get_from_coordinates(lat, lng), mimetype='application/json')


@mod_weather.route('/city/<city>', methods=['GET', 'POST'])
def get_weather_by_city(city):
    return jsonify(eval(WeatherManager().get_from_city(str(city))))
