from flask import Flask, Blueprint, render_template
from flask_restx import Api, Resource

app = Flask(
    __name__ )
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/')
app.register_blueprint(blueprint)

@api.route('/<device>/<metric>')
@api.doc(params={'device': 'device name', 'metric': 'sensor topic'})
class Device(Resource):
  def get(self, device, metric):
    return {}

  def post(self, device, metric):
    print("Device: " + device);

########## Web Page 

@app.route('/')
def root():
  return render_template('root.html')

if __name__ == '__main__':
  app.run(debug=True)




