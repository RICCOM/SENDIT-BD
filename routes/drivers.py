from flask import Flask, jsonify, request
from models import db, Driver

app = Flask(__name__)

@app.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = Driver.query.all()
    return jsonify([driver.to_dict() for driver in drivers])

@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = Driver.query.get_or_404(driver_id)
    return jsonify(driver.to_dict())

@app.route('/drivers', methods=['POST'])
def create_driver():
    data = request.json
    new_driver = Driver(name=data['name'], phone_number=data['phone_number'])
    db.session.add(new_driver)
    db.session.commit()
    return jsonify(new_driver.to_dict()), 201

@app.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    driver = Driver.query.get_or_404(driver_id)
    data = request.json
    driver.name = data.get('name', driver.name)
    driver.phone_number = data.get('phone_number', driver.phone_number)
    db.session.commit()
    return jsonify(driver.to_dict())

@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    driver = Driver.query.get_or_404(driver_id)
    db.session.delete(driver)
    db.session.commit()
    return jsonify({"message": "Driver deleted"}), 204
