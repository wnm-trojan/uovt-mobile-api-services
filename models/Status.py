"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Application status.
"""

from app import app, db

class Status(db.Model):
    __tablename__ = 'tbl_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status_code = db.Column(db.Integer, unique=True, nullable=False)
    status_name = db.Column(db.String(250), nullable=False)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    imei_code = db.Column(db.String(200))
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
