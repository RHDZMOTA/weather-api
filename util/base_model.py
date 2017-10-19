import json
from datetime import datetime
from google.appengine.ext import ndb as db


class WeatherJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y/%m/%d %H:%M:%S")
        return json.JSONEncoder.default(self, obj)


class SimpleModel(object):

    def to_dict(self):
        return self.__dict__

    def jsonify(self):
        return json.dumps(self.to_dict(), cls=WeatherJsonEncoder)


class SerializableModel(db.Model):

    def jsonify(self):
        return json.dumps(self.to_dict(), cls=WeatherJsonEncoder)

    def build(self):
        self.put()
        return self
