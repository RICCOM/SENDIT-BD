#Admin-only Decorator for Protected Routes
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify
from app.models import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        if not user.is_admin:
            return jsonify(msg='Admins only!'), 403
        return fn(*args, **kwargs)
    return wrapper