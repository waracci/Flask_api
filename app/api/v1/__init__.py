from flask_restful import Api
from flask import Blueprint

from .views import Carts as stuff


version1 = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(version1)
api.add_resource(stuff, '/cart', '/cart/<cart_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

