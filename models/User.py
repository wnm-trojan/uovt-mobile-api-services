"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Application users.
"""

from app import app, db
from models.Role import Role

class User(db.Model):
    __tablename__ = 'tbl_users'

    id = db.Column(db.Integer, primary_key=True)
    x_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    contact_no = db.Column(db.String(50), nullable=False)
    role_code = db.Column(db.String(20), db.ForeignKey('tbl_roles.role_code'), nullable=False)
    roles = db.relationship('Role', backref='tbl_users', uselist=False)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    imei_code = db.Column(db.String(200))
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
