from flask import Flask, jsonify, request
from models import db, ParcelType

app = Flask(__name__)

@app.route('/parcel_types', methods=['GET'])
def get_parcel_types():
    parcel_types = ParcelType.query.all()
    return jsonify([parcel_type.to_dict() for parcel_type in parcel_types])

@app.route('/parcel_types/<int:parcel_type_id>', methods=['GET'])
def get_parcel_type(parcel_type_id):
    parcel_type = ParcelType.query.get_or_404(parcel_type_id)
    return jsonify(parcel_type.to_dict())

@app.route('/parcel_types', methods=['POST'])
def create_parcel_type():
    data = request.json
    new_parcel_type = ParcelType(type_name=data['type_name'], weight_range=data['weight_range'], price=data['price'])
    db.session.add(new_parcel_type)
    db.session.commit()
    return jsonify(new_parcel_type.to_dict()), 201

@app.route('/parcel_types/<int:parcel_type_id>', methods=['PUT'])
def update_parcel_type(parcel_type_id):
    parcel_type = ParcelType.query.get_or_404(parcel_type_id)
    data = request.json
    parcel_type.type_name = data.get('type_name', parcel_type.type_name)
    parcel_type.weight_range = data.get('weight_range', parcel_type.weight_range)
    parcel_type.price = data.get('price', parcel_type.price)
    db.session.commit()
    return jsonify(parcel_type.to_dict())

@app.route('/parcel_types/<int:parcel_type_id>', methods=['DELETE'])
def delete_parcel_type(parcel_type_id):
    parcel_type = ParcelType.query.get_or_404(parcel_type_id)
    db.session.delete(parcel_type)
    db.session.commit()
    return jsonify({"message": "Parcel type deleted"}), 204
