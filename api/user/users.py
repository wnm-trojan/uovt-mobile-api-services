"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - User controller.
"""

from app import app, db
from flask import jsonify, request
from models.User import User
from models.Role import Role
from schemas.UserSchema import UserSchema
from services.auth import get_auth_user
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc
from werkzeug.security import generate_password_hash
import uuid

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# get all roles
@app.route('/users', methods=['GET'])
@jwt_required
def get_all_users():
    users = User.query.filter_by().all()
    return {'data': users_schema.dump(users),'status': 200}, 200

# get by id
@app.route('/users/<x_id>', methods=['GET'])
@jwt_required
def get_user_by_x_id(x_id):
    user = User.query.filter_by(x_id=x_id).first()

    if not user:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': user_schema.dump(user),'status': 200}, 200

# create an user
@app.route('/users', methods=['POST'])
@app.validate( 'users', 'users')
def register_user():
    payload = request.get_json()
    role = Role.query.filter_by(role_code=payload['role'].upper()).first()

    if not role:
        return jsonify({'error' : 'Role not found!','status': 404}), 404

    try:
        user =  User(x_id = str(uuid.uuid4()),
                    username = payload['username'].upper(),
                    password = generate_password_hash(payload['password'].encode('utf-8')),
                    firstname = payload['firstname'],
                    lastname = payload['lastname'],
                    email = payload['email'],
                    contact_no = payload['contact_no'],
                    role_code = role.role_code,
                    longitude=payload['longitude'],
                    latitude=payload['latitude'],
                    imei_code=payload['imei_code'],
                    status = 1)

        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'User already exists!','status': 400}), 400

    return jsonify({'message' : 'New user created!','status': 200}), 200

# update an user
@app.route('/users/<x_id>', methods=['PUT'])
@app.validate('users', 'users')
@jwt_required
def update_user(x_id):
    
    payload = request.get_json()
    role = Role.query.filter_by(role_code=payload['role'].upper()).first()
    if not role:
        return jsonify({'error' : 'Role not found!','status': 404}), 404

    user = User.query.filter_by(x_id=x_id).first()
    if not user: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        try:
            user.username = payload['username']
            if 'password' not in payload: 
                user.password = user.password
            else: 
                if not payload['password']:
                    user.password = user.password
                else:
                    user.password = payload['password']

            user.firstname = payload['firstname']
            user.lastname = payload['lastname']
            user.email = payload['email']
            user.contact_no = payload['contact_no']
            user.role_code = payload['role']
            user.longitude=payload['longitude']
            user.latitude=payload['latitude']
            user.imei_code=payload['imei_code']
            user.status = payload['status']
            user.updated_by = get_jwt_identity()

            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        

    return jsonify({'message' : 'User updated!','status': 200}), 200

# delete user
@app.route('/users/<x_id>', methods=['DELETE'])
@jwt_required
def delete_user(x_id):
    user = User.query.filter_by(x_id=x_id).first()
    if not user: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        payload = request.get_json()
        try:
            user.status = 0
            user.updated_by = get_jwt_identity()
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'User deleted!','status': 200}), 200
