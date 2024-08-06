from flask import jsonify, request
from app import db
from app.models import User
from app.auth import bp

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'must include username, email and password fields'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'please use a different username'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'please use a different email address'}), 400
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201