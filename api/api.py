from flask import Blueprint

# Import Resources
from . import Sensor

class Api(Blueprint):
  PREFIX = '/api'

  def __init__(self, app):
    super.__init__(
      'api',
      __name__,
      template_folder='templates',
      static_folder='static'
    )

    self.api = Api(app=self, prefix=self.PREFIX)
    self.api.add_resource(Sensor, '/sensor')
