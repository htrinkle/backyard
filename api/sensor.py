from flask_restful import Resource

class Sensor(Resource):
  def get(self):
    return "GET"
  def post(self):
    return "POSTed"

