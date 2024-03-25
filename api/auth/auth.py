"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Authentication manager.
"""

from app import app, jwt
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from models.User import User
from schemas.UserSchema import UserSchema
from services.auth import authenticate
import datetime

# Claims the user detils in the access token
@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    user = User.query.filter_by(username=identity).first()
    return {
        'roles': UserSchema().dump(user)
    }

# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token.
@app.route('/auth', methods=['POST'])
def authentication():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request!", "status": 400}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"error": "Missing username parameter!", "status": 400}), 400
    if not password:
        return jsonify({"error": "Missing password parameter!", "status": 400}), 400

    if not authenticate(username, password):
        return jsonify({"error": "Invalid username or password!", "status": 401}), 401

    # Identity can be any data that is json serializable
    expires = datetime.timedelta(days=1)
    access_token = create_access_token(identity=username, expires_delta=expires)
    return jsonify(access_token=access_token), 200