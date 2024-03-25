"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Application crisis status.
"""

from app import app, db

class CrisisStatus(db.Model):
    __tablename__ = 'tbl_user_crisis_statuses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('tbl_users.x_id'), nullable=False)
    users = db.relationship('User', backref='tbl_crisis_statuses', uselist=False)
    status_code = db.Column(db.Integer, db.ForeignKey('tbl_statuses.status_code'), nullable=False)
    statuses = db.relationship('Status', backref='tbl_crisis_statuses', uselist=False)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    imei_code = db.Column(db.String(200))
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())