#This service handles user registration, login, and authorization.
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import User
from app import db

def register_user(username, email, password):
    if User.query.filter_by(email=email).first() is not None:
        return {'message': 'User already exists'}, 400
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User created successfully'}, 201

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200
    return {'message': 'Invalid credentials'}, 401

@jwt_required()
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    return {'message': 'User not found'}, 404

@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    return get_user_by_id(user_id)
