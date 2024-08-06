from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash,generate_password_hash
from models import db, User
import jwt
import datetime

auth_bp = Blueprint('auth_bp', __name__)

SECRET_KEY = 'your_secret_key'

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY)
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid username or password'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token is missing'}), 403
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        current_user = User.query.get(data['user_id'])
    except:
        return jsonify({'error': 'Token is invalid or expired'}), 403
    return jsonify({'message': 'This is a protected route', 'user': current_user.to_dict()})