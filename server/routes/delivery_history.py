#This service handles the history of drivers and their activities.
from models import DriverHistory
from app import db

def create_driver_history(driver_id, parcel_id, status, location):
    new_history = DriverHistory(driver_id=driver_id, parcel_id=parcel_id, status=status, location=location)
    db.session.add(new_history)
    db.session.commit()
    return {'message': 'Driver history created successfully'}, 201

def get_driver_history_by_id(history_id):
    history = DriverHistory.query.get(history_id)
    if history:
        return history
    return {'message': 'Driver history not found'}, 404

def get_all_driver_histories():
    return DriverHistory.query.all()

def get_histories_by_driver(driver_id):
    return DriverHistory.query.filter_by(driver_id=driver_id).all()
