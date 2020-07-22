from flask import Flask, Blueprint, render_template
from flask_restx import Api, Resource, reqparse
import time

deviceParser = reqparse.RequestParser()
deviceParser.add_argument('temp', type=float)
deviceParser.add_argument('key', type=str)

app = Flask(
    __name__ )
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/')
app.register_blueprint(blueprint)

key_map = {
'hansnodemcu': '1234abcd'
}

temperature = []

@api.route('/<device>')
@api.doc(params={'device': 'device name', 'key':'api key'})
class Device(Resource):
  def get(self, device):
    args = deviceParser.parse_args()
    if device not in key_map.keys():
      return "", 401
    if key_map[device] != args['key']:
      return "", 401
    result = {}
    for i in range (len(temperature)):
      result[temperature[i][0]] = temperature[i][1];
    
    return result

  @api.doc(params={'temp': '23.56'})
  def post(self, device):
    args = deviceParser.parse_args()
    if device not in key_map.keys():
      return "", 401
    if key_map[device] != args['key']:
      return "", 401
    now = time.time();
    temperature.append( (now,args['temp']) )
    temperature = temperature[-1000:]
    return "OK", 200

########## Web Page 

@app.route('/')
def root():
  return render_template('root.html')

if __name__ == '__main__':
  app.debug = true
  app.run(ssl_context='adhoc')




