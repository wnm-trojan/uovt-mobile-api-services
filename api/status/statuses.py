"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Status controller.
"""

from app import app, db
from flask import jsonify, request
from models.Status import Status
from schemas.StatusSchema import StatusSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

status_schema = StatusSchema()
statuses_schema = StatusSchema(many=True)

# get all statuses
@app.route('/statuses', methods=['GET'])
@jwt_required
def get_statuses():
    statuses = Status.query.all()
    return {'data': statuses_schema.dump(statuses), 'status': 200}, 200


# get status by status code
@app.route('/statuses/<code>', methods=['GET'])
@jwt_required
def get_status_by_status_code(code):
    status = Status.query.filter_by(status_code=code).first()

    if not status:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': status_schema.dump(status),'status': 200}, 200


# create a status
@app.route('/statuses', methods=['POST'])
@jwt_required
def create_status():
    payload = request.get_json()

    try:
        status = Status(status_code=payload['status_code'],
                        status_name=payload['status_name'],
                        longitude=payload['longitude'],
                        latitude=payload['latitude'],
                        imei_code=payload['imei_code'],
                        status=1,
                        created_by='admin')

        db.session.add(status)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Status already exists!','status': 400}), 400

    return jsonify({'message' : 'New status created!','status': 200}), 200


# update a status
@app.route('/statuses/<code>', methods=['PUT'])
@jwt_required
def update_status(code):
    status = Status.query.filter_by(status_code=code).first()

    if not status:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        payload = request.get_json()
        try:
            status.status_code = payload['status_code']
            status.status_name = payload['status_name']
            status.longitude=payload['longitude']
            status.latitude=payload['latitude']
            status.imei_code=payload['imei_code']
            status.status = payload['status']
            status.updated_by = get_jwt_identity()

            db.session.add(status)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        
    return jsonify({'message' : 'Status updated!','status': 200}), 200
    

# delete a status
@app.route('/statuses/<code>', methods=['DELETE'])
@jwt_required
def delete_status(code):
    status = Status.query.filter_by(status_code=code).first()
    if not status: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        try:
            db.session.delete(status)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'Status has been deleted!','status': 200}), 200
