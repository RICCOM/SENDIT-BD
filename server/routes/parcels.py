from flask import Flask, jsonify, request
from models import db, Parcel

app = Flask(__name__)

@app.route('/parcels', methods=['GET'])
def get_parcels():
    parcels = Parcel.query.all()
    return jsonify([parcel.to_dict() for parcel in parcels])

@app.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    return jsonify(parcel.to_dict())

@app.route('/parcels', methods=['POST'])
def create_parcel():
    data = request.json
    new_parcel = Parcel(
        user_id=data['user_id'],
        driver_id=data.get('driver_id'),
        weight=data['weight'],
        pickup_address=data['pickup_address'],
        pickup_lat=data['pickup_lat'],
        pickup_lng=data['pickup_lng'],
        destination_address=data['destination_address'],
        destination_lat=data['destination_lat'],
        destination_lng=data['destination_lng'],
        status=data['status'],
        present_location=data['present_location'],
        present_location_lat=data['present_location_lat'],
        present_location_lng=data['present_location_lng']
    )
    db.session.add(new_parcel)
    db.session.commit()
    return jsonify(new_parcel.to_dict()), 201

@app.route('/parcels/<int:parcel_id>', methods=['PUT'])
def update_parcel(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    data = request.json
    parcel.weight = data.get('weight', parcel.weight)
    parcel.pickup_address = data.get('pickup_address', parcel.pickup_address)
    parcel.pickup_lat = data.get('pickup_lat', parcel.pickup_lat)
    parcel.pickup_lng = data.get('pickup_lng', parcel.pickup_lng)
    parcel.destination_address = data.get('destination_address', parcel.destination_address)
    parcel.destination_lat = data.get('destination_lat', parcel.destination_lat)
    parcel.destination_lng = data.get('destination_lng', parcel.destination_lng)
    parcel.status = data.get('status', parcel.status)
    parcel.present_location = data.get('present_location', parcel.present_location)
    parcel.present_location_lat = data.get('present_location_lat', parcel.present_location_lat)
    parcel.present_location_lng = data.get('present_location_lng', parcel.present_location_lng)
    db.session.commit()
    return jsonify(parcel.to_dict())

@app.route('/parcels/<int:parcel_id>', methods=['DELETE'])
def delete_parcel(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    db.session.delete(parcel)
    db.session.commit()
    return jsonify({"message": "Parcel deleted"}), 204
