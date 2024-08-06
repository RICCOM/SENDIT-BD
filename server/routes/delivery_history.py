
from flask import Flask, jsonify, request
from models import db, DeliveryHistory

app = Flask(_name_)

@app.route('/delivery_history', methods=['GET'])
def get_delivery_histories():
    histories = DeliveryHistory.query.all()
    return jsonify([history.to_dict() for history in histories])

@app.route('/delivery_history/<int:history_id>', methods=['GET'])
def get_delivery_history(history_id):
    history = DeliveryHistory.query.get_or_404(history_id)
    return jsonify(history.to_dict())

@app.route('/delivery_history', methods=['POST'])
def create_delivery_history():
    data = request.json
    new_history = DeliveryHistory(
        parcel_id=data['parcel_id'],
        status=data['status'],
        location=data['location'],
        location_lat=data['location_lat'],
        location_lng=data['location_lng'],
        updated_at=data.get('updated_at')
    )
    db.session.add(new_history)
    db.session.commit()
    return jsonify(new_history.to_dict()), 201

@app.route('/delivery_history/<int:history_id>', methods=['PUT'])
def update_delivery_history(history_id):
    history = DeliveryHistory.query.get_or_404(history_id)
    data = request.json
    history.status = data.get('status', history.status)
    history.location = data.get('location', history.location)
    history.location_lat = data.get('location_lat', history.location_lat)
    history.location_lng = data.get('location_lng', history.location_lng)
    history.updated_at = data.get('updated_at', history.updated_at)
    db.session.commit()
    return jsonify(history.to_dict())

@app.route('/delivery_history/<int:history_id>', methods=['DELETE'])
def delete_delivery_history(history_id):
    history = DeliveryHistory.query.get_or_404(history_id)
    db.session.delete(history)
    db.session.commit()
    return jsonify({"message": "Delivery history deleted"}), 204