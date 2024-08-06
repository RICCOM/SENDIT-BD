from flask import jsonify, request
from app import db
from app.models import User
from app.auth import bp
from flask_jwt_extended import jwt_required, get_jwt_identity

@bp.route('/change_password', methods=['POST'])
@jwt_required()
def change_password():
    data = request.get_json() or {}
    if 'old_password' not in data or 'new_password' not in data:
        return jsonify({'error': 'must include old_password and new_password fields'}), 400
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    if not user.check_password(data['old_password']):
        return jsonify({'error': 'Invalid old password'}), 400
    user.set_password(data['new_password'])
    db.session.commit()
    return jsonify({'message': 'Password changed successfully'}), 200