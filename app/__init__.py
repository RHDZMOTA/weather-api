from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.appengine.ext import db

app = Flask(__name__)
app.config.from_object('app_config')

# Google OCR
from app.mod_weather.controller import mod_weather as weather
app.register_blueprint(weather)
