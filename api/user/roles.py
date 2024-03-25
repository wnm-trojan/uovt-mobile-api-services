"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - User role controller.
"""

from app import app
from flask import jsonify 
from models.Role import Role
from schemas.RoleSchema import RoleSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# get all roles
@app.route('/roles', methods=['GET'])
@jwt_required
def get_roles():
    users = Role.query.all()
    return {'data': roles_schema.dump(users),'status': 200}, 200