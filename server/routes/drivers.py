#This service handles driver registration, login, and management.
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import Driver
from app import db

def register_driver(username, email, password):
    if Driver.query.filter_by(email=email).first() is not None:
        return {'message': 'Driver already exists'}, 400
    
    hashed_password = generate_password_hash(password)
    new_driver = Driver(username=username, email=email, password=hashed_password)
    db.session.add(new_driver)
    db.session.commit()
    return {'message': 'Driver created successfully'}, 201

def login_driver(email, password):
    driver = Driver.query.filter_by(email=email).first()
    if driver and check_password_hash(driver.password, password):
        access_token = create_access_token(identity=driver.id)
        return {'access_token': access_token}, 200
    return {'message': 'Invalid credentials'}, 401

@jwt_required()
def get_driver_by_id(driver_id):
    driver = Driver.query.get(driver_id)
    if driver:
        return driver
    return {'message': 'Driver not found'}, 404

@jwt_required()
def get_current_driver():
    driver_id = get_jwt_identity()
    return get_driver_by_id(driver_id)
