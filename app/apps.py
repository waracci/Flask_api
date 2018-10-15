from flask import Flask, Blueprint
from flask_restful import Resource, Api


from instance.config import app_config
# from .api.v1.views import Carts as stuff

version_1_blueprint = Blueprint('api', __name__)
api = Api(version_1_blueprint)

def create_app(config_name):
    app=Flask(__name__, instance_relative_config=True)

    from .api.v1 import version1 as v1

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)
    return app