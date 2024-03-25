"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Crisis Status controller.
"""

from app import app, db
from flask import jsonify, request
from models.CrisisStatus import CrisisStatus
from models.User import User
from models.Status import Status
from schemas.CrisisStatusSchema import CrisisStatusSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

crisisstatus_schema = CrisisStatusSchema()
crisisstatuses_schema = CrisisStatusSchema(many=True)

# get all crisis statuses
@app.route('/crisis-statuses', methods=['GET'])
@jwt_required
def get_crisisstatuses():
    crisisstatuses = CrisisStatus.query.all()
    return {'data': crisisstatuses_schema.dump(crisisstatuses), 'status': 200}, 200


# get crisis statuses by user id
@app.route('/crisis-statuses/<x_id>', methods=['GET'])
@jwt_required
def get_crisisstatuses_by_user_id(x_id):
    crisisstatus = CrisisStatus.query.filter_by(user_id=x_id)   
    return {'data': crisisstatuses_schema.dump(crisisstatus),'status': 200}, 200


# create a crisis statuses
@app.route('/crisis-statuses', methods=['POST'])
@jwt_required
def create_crisisstatus():
    payload = request.get_json()

    user = User.query.filter_by(x_id=payload['user_id']).first()
    if not user: 
        return jsonify({'error' : 'User not found!','status': 404}), 404

    status = Status.query.filter_by(status_code=payload['status_code']).first()
    if not status:
        return jsonify({'error' : 'Status code not found!','status': 404}), 404

    try:
        crisisstatus = CrisisStatus(user_id=user.x_id,
                        status_code=status.status_code,
                        longitude=payload['longitude'],
                        latitude=payload['latitude'],
                        imei_code=payload['imei_code'],
                        created_by='admin')

        db.session.add(crisisstatus)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Status already exists!','status': 400}), 400

    return jsonify({'message' : 'New status created!','status': 200}), 200
