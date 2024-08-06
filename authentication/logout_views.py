from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Handle logout logic here (e.g., revoke tokens, etc.)
    return jsonify({'msg': 'Successfully logged out'}), 200
