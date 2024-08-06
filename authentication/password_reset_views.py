from flask import Blueprint, request, jsonify, url_for
from werkzeug.security import generate_password_hash
from .models import User, db
from .email_utils import send_email
from .tokens import generate_password_reset_token, confirm_password_reset_token


password_reset_bp = Blueprint('password_reset', __name__)


@password_reset_bp.route('/request-reset', methods=['POST'])
def request_reset():
    data = request.json
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'msg': 'No account with that email'}), 404

    token = generate_password_reset_token(email)
    reset_url = url_for(
        'password_reset.reset_password',
        token=token,
        _external=True
    )

    send_email(
        email,
        'Password Reset Request',
        'reset_email',
        reset_url=reset_url
    )

    return jsonify({'msg': 'Password reset link sent'}), 200


@password_reset_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.json
    new_password = data.get('new_password')

    try:
        email = confirm_password_reset_token(token)
    except Exception:
        return jsonify({'msg': 'The reset link is invalid or has expired.'}), 400

    user = User.query.filter_by(email=email).first_or_404()
    hashed_password = generate_password_hash(new_password, method='sha256')
    user.password = hashed_password
    db.session.commit()

    message = 'Password has been updated successfully.'
    response = jsonify({'msg': message})
    return response, 200
