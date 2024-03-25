"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Authentication Service
"""
from app import app
from models.User import User
from werkzeug.security import check_password_hash
from flask import request
import jwt

def authenticate(username, password):
    user = User.query.filter_by(username=username.upper(), status=1).first()
    if user and check_password_hash(user.password, password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)

def get_auth_user():
    token = request.headers.get('Authorization')
    data = jwt.decode(token, app.config['SECRET_KEY'], 'utf-8', algorithms=['HS256'])
    return User.query.filter_by(id=data['identity']).first()