from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from .models import User

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'msg': 'Invalid email or password'}), 401

    if not user.verified:
        return jsonify({'msg': 'Email not verified'}), 403

    access_token = create_access_token(identity={'user_id': user.id})
    return jsonify(access_token=access_token), 200
