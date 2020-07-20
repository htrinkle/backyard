from flask import Flask, Blueprint, render_template
from flask_restplus import Api, Resource
# from webargs import fields, validate
# from webargs.flaskparser import use_kwargs, use_args, parser

import datetime as dt

app = Flask(
  __name__, 
  static_url_path = "/static", 
  static_folder = "static",
  template_folder = "templates"
)

########## API 

bp = Blueprint(
  'api',
  __name__,
)

api = Api(app=bp)

readings = {
      '2020-01-02T16:34:21':{
        'temp' : 235,
        'humidity' : 850
      },
      '2020-01-02T17:34:21':{
        'temp' : 135,
        'humidity' : 550
      }
    }


class Sensor(Resource):
  #@api.expect(sensor_arg, validate=True)
  def put(self, id):
    """ Install a new sensor """
    return {"sensor":"added"}, 201 
  

class Measurement(Resource):
  #@api.expect(measurement_arg, validate=True)
  def put(self, id):
    """ Return list of all sensor readings. """
    return {"measurement":"added"}, 201 

class History(Resource):
  #@api.expect(history_arg, validate=True)
  def get(self):
    """ Return filtered list of measurements """
    return {
      'happy':'now'
    }, 200

api.add_resource(Measurement, '/sensor/<id>/measurement')
api.add_resource(Sensor, '/sensor/<id>')
api.add_resource(History, '/history')

app.register_blueprint(bp, url_prefix='/api')

########## Web Page 

@app.route('/')
def root():
  return render_template('root.html')

if __name__ == '__main__':
  app.run(debug=True)



