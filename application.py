from flask import Flask, Blueprint, render_template
from flask_restx import Api, Resource, reqparse
import time
import json

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

store = {
't': []
}

try:
    with open('data.txt') as json_file:
        store = json.load(json_file);
except:
    print("data.txt not found - empty data")

@api.route('/<device>')
@api.doc(params={'device': 'device name', 'key':'api key'})
class Device(Resource):
  def get(self, device):
    args = deviceParser.parse_args()

    if device not in key_map.keys():
      return "", 401
    if key_map[device] != args['key']:
      return "", 401

    data = store['t']
    if len(data) == 0:
      return {}

    time_list = []
    temp_list = []
    for x in data:
      time_list += [x[0]]
      temp_list += [x[1]]
      
    return {'temp': ','.join(map(str, temp_list)) , 'time': ','.join(map(str, time_list))}

  @api.doc(params={'temp': '23.56'})
  def post(self, device):
    args = deviceParser.parse_args()
    print(args)
    if device not in key_map.keys():
      return "", 401
    if key_map[device] != args['key']:
      return "", 401

    data = store['t']
    now = time.time()
    data = data + [[now,args['temp']]]

    if len(data) > 1000:
        data = data[-1000:]
    
    store['t'] = data

    with open('data.txt', 'w') as json_file:
        json.dump(store, json_file);

    return "OK", 200

########## Web Page 

@app.route('/')
def root():
  return render_template('root.html')

if __name__ == '__main__':
  app.run()




