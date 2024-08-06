from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, db

password_bp = Blueprint('password', __name__)

@password_bp.route('/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    data = request.json
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    current_user = get_jwt_identity()
    user = User.query.get(current_user['user_id'])

    if not check_password_hash(user.password, old_password):
        return jsonify({'msg': 'Old password is incorrect'}), 400

    hashed_new_password = generate_password_hash(new_password, method='sha256')
    user.password = hashed_new_password
    db.session.commit()

    return jsonify({'msg': 'Password updated successfully'}), 200
