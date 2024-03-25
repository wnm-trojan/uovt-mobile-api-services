"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Application news.
"""

from app import app, db

class News(db.Model):
    __tablename__ = 'tbl_news'

    id = db.Column(db.Integer, primary_key=True)
    news_code = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(25), nullable=False)
    news_id = db.Column(db.String(1000), nullable=False)
    link = db.Column(db.String(1000), nullable=False)
    imgSrc = db.Column(db.String(1000), nullable=False)
    placeholder = db.Column(db.String(500), nullable=False)
    summary = db.Column(db.String(2000), nullable=False)
    contentLength = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())