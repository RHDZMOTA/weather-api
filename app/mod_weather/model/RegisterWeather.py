import time
from util.base_model import SerializableModel, db


class WeatherQuery(SerializableModel):
    created_at = db.DateTimeProperty(auto_now_add=True)
    unix_query = db.IntegerProperty(required=True)
    calculation_unix_utc = db.IntegerProperty(required=True)
    city_name = db.StringProperty(required=True)
    country = db.StringProperty(required=True)
    lat = db.FloatProperty(required=True)
    lng = db.FloatProperty(required=True)
    humidity = db.IntegerProperty()
    pressure = db.IntegerProperty()
    temp_kelvin = db.FloatProperty()
    temp_kelvin_min = db.FloatProperty()
    temp_kelvin_max = db.FloatProperty()
    visibility = db.IntegerProperty()
    cloud_percentage = db.IntegerProperty()
    wind_speed = db.FloatProperty()
    wind_degree = db.FloatProperty()
    sunrise_unix_utc = db.IntegerProperty()
    sunset_unix_utc = db.IntegerProperty()
    weather_main = db.StringProperty(required=True)
    weather_description = db.StringProperty()


class RegisterWeather(object):

    def __init__(self, data):
        self.data = data
        self.epoch_time = int(time.time())

    def save(self):
        return WeatherQuery(
            unix_query=self.epoch_time,
            lat=float(self.data["coord"].get("lat")),
            lng=float(self.data["coord"].get("lon")),
            humidity=int(self.data["main"].get("humidity")),
            pressure=int(self.data["main"].get("pressure")),
            temp_kelvin=float(self.data["main"].get("temp")),
            temp_kelvin_min=float(self.data["main"].get("temp_min")),
            temp_kelvin_max=float(self.data["main"].get("temp_max")),
            visibility=int(self.data["visibility"]),
            cloud_percentage=int(self.data["clouds"].get("all")),
            wind_speed=float(self.data["wind"].get("speed")),
            wind_degree=float(self.data["wind"].get("deg")),
            sunrise_unix_utc=int(self.data["sys"].get("sunrise")),
            sunset_unix_utc=int(self.data["sys"].get("sunset")),
            calculation_unix_utc=int(self.data["dt"]),
            country=str(self.data["sys"].get("country")),
            city_name=str(self.data.get("name")),
            weather_main=[str(i.get("main")) for i in self.data["weather"]][0],
            weather_description=[str(i.get("description")) for i in self.data["weather"]][0]
        ).build()
