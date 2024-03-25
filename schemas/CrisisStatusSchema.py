"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Crisis Status schema.
"""

from flask import request
from app import ma
from models.CrisisStatus import CrisisStatus
from schemas.UserSchema import UserSchema
from schemas.StatusSchema import StatusSchema

class CrisisStatusSchema(ma.Schema):

    users = ma.Nested(UserSchema)
    statuses = ma.Nested(StatusSchema)

    class Meta:
        fields = ('user_id', 'student_reg_no', 'status_code', 'status_name', 'longitude', 'latitude', 'imei_code', 'status')