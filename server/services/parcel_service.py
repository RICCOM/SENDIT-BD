#This service handles parcel creation, updates, and retrieval.
from models import Parcel, User
from app import db
from services.notification_service import notify_status_change, notify_location_change

def create_parcel(user_id, weight, destination, pickup_location):
    new_parcel = Parcel(
        weight=weight,
        destination=destination,
        pickup_location=pickup_location,
        present_location=pickup_location,
        status='Pending',
        user_id=user_id
    )
    db.session.add(new_parcel)
    db.session.commit()
    return {'message': 'Parcel created successfully'}, 201

def change_parcel_destination(parcel_id, user_id, new_destination):
    parcel = Parcel.query.get(parcel_id)
    if parcel is None or parcel.user_id != user_id or parcel.status == 'Delivered':
        return {'message': 'Parcel not found or action not allowed'}, 400
    
    parcel.destination = new_destination
    db.session.commit()
    return {'message': 'Parcel destination updated successfully'}

def cancel_parcel(parcel_id, user_id):
    parcel = Parcel.query.get(parcel_id)
    if parcel is None or parcel.user_id != user_id or parcel.status == 'Delivered':
        return {'message': 'Parcel not found or action not allowed'}, 400
    
    parcel.status = 'Cancelled'
    db.session.commit()
    return {'message': 'Parcel cancelled successfully'}

def update_parcel_status(parcel_id, status):
    parcel = Parcel.query.get(parcel_id)
    if parcel is None:
        return {'message': 'Parcel not found'}, 400
    
    parcel.status = status
    db.session.commit()
    notify_status_change(parcel)
    return {'message': 'Parcel status updated successfully'}

def update_parcel_location(parcel_id, location):
    parcel = Parcel.query.get(parcel_id)
    if parcel is None:
        return {'message': 'Parcel not found'}, 400
    
    parcel.present_location = location
    db.session.commit()
    notify_location_change(parcel)
    return {'message': 'Parcel location updated successfully'}

def get_parcel_by_id(parcel_id):
    return Parcel.query.get(parcel_id)

def get_all_parcels_by_user(user_id):
    return Parcel.query.filter_by(user_id=user_id).all()

def get_all_parcels():
    return Parcel.query.all()
