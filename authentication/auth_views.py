from flask import Blueprint, request, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
from .email_utils import send_email
from .tokens import generate_confirmation_token, confirm_token
from flask_jwt_extended import create_access_token, jwt_required

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'Email is already in use'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Generate email verification token
    token = generate_confirmation_token(email)
    verification_url = url_for(
        'auth.verify_email', token=token, _external=True
    )
    
    # Send verification email
    send_email(
        email,
        'Please Verify Your Email',
        'verify_email',
        verification_url=verification_url
    )

    return jsonify({
        'msg': 'User created successfully. Please check your email to verify your account.'
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'msg': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=email)
    return jsonify({'access_token': access_token}), 200


@auth_bp.route('/verify-email/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = confirm_token(token)
    except Exception:
        return jsonify({
            'msg': 'The verification link is invalid or has expired.'
        }), 400

    user = User.query.filter_by(email=email).first_or_404()
    if user.is_verified:
        return jsonify({'msg': 'Account already verified'}), 200

    user.is_verified = True
    db.session.commit()
    return jsonify({'msg': 'Email verified successfully'}), 200


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({'msg': 'Logout successful'}), 200
