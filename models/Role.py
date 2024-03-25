"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Application user roles.
"""

from app import app, db

class Role(db.Model):
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(10), unique=True)
    role_name = db.Column(db.String(50), unique=True)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
