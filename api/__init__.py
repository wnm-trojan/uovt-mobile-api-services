"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Create an application.
"""

import os
from flask import Flask, Response
from core.middleware import Middleware
from flask_jsonschema_validator import JSONSchemaValidator
from flask_cors import CORS
import datetime

# Override response format
class Response(Response):
    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    def __init__(self, response, **kwargs):
        return super(Response, self).__init__(response, **kwargs)

    @classmethod
    def force_type(cls, response, environ=None):
        pass

# Load flask with override format
class Flask(Flask):
    response_class = Response

def create_app():
    app = Flask(__name__)

    # Middleware
    app.wsgi_app = Middleware(app.wsgi_app, prefix='/api/v1')

    # add CORS support
    CORS(app)

    # Authentication
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    # Request Validator
    JSONSchemaValidator(app=app, root="schemas/validations")

    return app
