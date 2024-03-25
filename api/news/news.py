"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - News controller.
"""

from app import app, db
from flask import jsonify, request
from models.News import News
from schemas.NewsSchema import NewsSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

news_schema = NewsSchema()
newsall_schema = NewsSchema(many=True)

# get all news
@app.route('/news', methods=['GET'])
@jwt_required
def get_all_news():
    newsall = News.query.all()
    return {'data': newsall_schema.dump(newsall), 'status': 200}, 200


# get news by news code
@app.route('/news/<code>', methods=['GET'])
@jwt_required
def get_news_by_news_code(code):
    news = News.query.filter_by(news_code=code).first()

    if not news:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': news_schema.dump(news),'status': 200}, 200


# create a news
@app.route('/news', methods=['POST'])
@jwt_required
def create_news():
    payload = request.get_json()

    try:
        news = News(news_code=payload['news_code'],
                        title=payload['title'],
                        author=payload['author'],
                        category=payload['category'],
                        news_id=payload['news_id'],
                        link=payload['link'],
                        imgSrc=payload['imgSrc'],
                        placeholder=payload['placeholder'],
                        summary=payload['summary'],
                        contentLength=payload['contentLength'],
                        status=1,
                        created_by='admin')

        db.session.add(news)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'News already exists!','status': 400}), 400

    return jsonify({'message' : 'New news created!','status': 200}), 200


# update a news
@app.route('/news/<code>', methods=['PUT'])
@jwt_required
def update_news(code):
    news = News.query.filter_by(news_code=code).first()

    if not news:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        payload = request.get_json()
        try:
            news.news_code = payload['news_code']
            news.title = payload['title']
            news.author = payload['author']
            news.category = payload['category']
            news.news_id = payload['news_id']
            news.link = payload['link']
            news.imgSrc = payload['imgSrc']
            news.placeholder = payload['placeholder']
            news.summary = payload['summary']
            news.contentLength = payload['contentLength']
            news.status = payload['status']
            news.updated_by = get_jwt_identity()

            db.session.add(news)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        
    return jsonify({'message' : 'News updated!','status': 200}), 200


# delete a news
@app.route('/news/<code>', methods=['DELETE'])
@jwt_required
def delete_news(code):
    news = News.query.filter_by(news_code=code).first()
    if not news: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        try:
            db.session.delete(news)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'News has been deleted!','status': 200}), 200