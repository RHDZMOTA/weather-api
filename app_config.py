import os
import json
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'secret'
SECRET_KEY = 'secret'
with open('client_secret.json') as secret_content:
    client_secrets_map = json.load(secret_content)

OWM_KEY = client_secrets_map["open-weather-map"].get("api-key")
OWM_COORDINATES = client_secrets_map["open-weather-map"].get("coordinates-url")
OWM_CITY = client_secrets_map["open-weather-map"].get("city-url")
UPDATE_SECONDS = 60*15
