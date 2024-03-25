"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - User schema.
"""

from flask import request
from app import ma
from models.User import User
from schemas.RoleSchema import RoleSchema

class UserSchema(ma.Schema):

  roles = ma.Nested(RoleSchema)

  class Meta:
    fields = ('x_id', 'student_reg_no', 'username', 'firstname', 'lastname', 'email', 'contact_no', 'role_code', 'longitude', 'latitude', 'imei_code', 'status')
