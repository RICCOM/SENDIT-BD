from flask import Flask, jsonify, request
from models import db, Admin

app = Flask(_name_)

@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([admin.to_dict() for admin in admins])

@app.route('/admins/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return jsonify(admin.to_dict())

@app.route('/admins', methods=['POST'])
def create_admin():
    data = request.json
    new_admin = Admin(username=data['username'], email=data['email'], password_hash=data['password_hash'])
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(new_admin.to_dict()), 201

@app.route('/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    data = request.json
    admin.username = data.get('username', admin.username)
    admin.email = data.get('email', admin.email)
    admin.password_hash = data.get('password_hash', admin.password_hash)
    db.session.commit()
    return jsonify(admin.to_dict())

@app.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return jsonify({"message": "Admin deleted"}), 204