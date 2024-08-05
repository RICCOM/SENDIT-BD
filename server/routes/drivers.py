from flask import Flask, jsonify, request

app = Flask(__name__)


drivers = [
    {"id": 1, "name": "John Doe", "license_number": "XYZ1234", "vehicle": "Truck", "status": "active"},
    {"id": 2, "name": "Jane Smith", "license_number": "ABC5678", "vehicle": "Van", "status": "inactive"},
]

@app.route('/drivers', methods=['GET'])
def get_drivers():
    """Get all drivers."""
    return jsonify(drivers)

@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    """Get a specific driver by ID."""
    driver = next((d for d in drivers if d["id"] == driver_id), None)
    if driver:
        return jsonify(driver)
    return jsonify({"error": "Driver not found"}), 404

@app.route('/drivers', methods=['POST'])
def create_driver():
    """Create a new driver."""
    data = request.json
    new_driver = {
        "id": len(drivers) + 1,
        "name": data.get("name"),
        "license_number": data.get("license_number"),
        "vehicle": data.get("vehicle"),
        "status": data.get("status", "active")
    }
    drivers.append(new_driver)
    return jsonify(new_driver), 201

@app.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    """Update an existing driver."""
    driver = next((d for d in drivers if d["id"] == driver_id), None)
    if driver:
        data = request.json
        driver["name"] = data.get("name", driver["name"])
        driver["license_number"] = data.get("license_number", driver["license_number"])
        driver["vehicle"] = data.get("vehicle", driver["vehicle"])
        driver["status"] = data.get("status", driver["status"])
        return jsonify(driver)
    return jsonify({"error": "Driver not found"}), 404

@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    """Delete a driver."""
    global drivers
    drivers = [d for d in drivers if d["id"] != driver_id]
    return jsonify({"message": "Driver deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
