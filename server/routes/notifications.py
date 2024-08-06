from flask import Flask, jsonify, request
from models import db, Notification

app = Flask(_name_)

@app.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = Notification.query.all()
    return jsonify([notification.to_dict() for notification in notifications])

@app.route('/notifications/<int:notification_id>', methods=['GET'])
def get_notification(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    return jsonify(notification.to_dict())

@app.route('/notifications', methods=['POST'])
def create_notification():
    data = request.json
    new_notification = Notification(user_id=data['user_id'], parcel_id=data['parcel_id'], message=data['message'])
    db.session.add(new_notification)
    db.session.commit()
    return jsonify(new_notification.to_dict()), 201

@app.route('/notifications/<int:notification_id>', methods=['PUT'])
def update_notification(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    data = request.json
    notification.message = data.get('message', notification.message)
    db.session.commit()
    return jsonify(notification.to_dict())

@app.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    db.session.delete(notification)
    db.session.commit()
    return jsonify({"message": "Notification deleted"}), 204