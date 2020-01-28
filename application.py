from flask import Flask, Blueprint, render_template
from flask_restplus import Api, Resource

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

class Sensor(Resource):
  def get(self):
    return "GET Method on sensor"
  def post(self):
    return "POST Method on sensor"

api.add_resource(Sensor, '/sensor')
app.register_blueprint(bp, url_prefix='/api')

########## Web Page 

@app.route('/')
def root():
  return render_template('root.html')




