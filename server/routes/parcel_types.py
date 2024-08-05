from flask import Flask, jsonify, request

app = Flask(__name__)


parcel_types = [
    {"id": 1, "name": "Type A"},
    {"id": 2, "name": "Type B"},
]

@app.route('/parcel_types', methods=['GET'])
def get_parcel_types():
    """Get all parcel types."""
    return jsonify(parcel_types)

@app.route('/parcel_types/<int:type_id>', methods=['GET'])
def get_parcel_type(type_id):
    """Get a specific parcel type by ID."""
    parcel_type = next((t for t in parcel_types if t["id"] == type_id), None)
    if parcel_type:
        return jsonify(parcel_type)
    return jsonify({"error": "Parcel type not found"}), 404

@app.route('/parcel_types', methods=['POST'])
def create_parcel_type():
    """Create a new parcel type."""
    data = request.json
    new_type = {
        "id": len(parcel_types) + 1,
        "name": data.get("name")
    }
    parcel_types.append(new_type)
    return jsonify(new_type), 201

@app.route('/parcel_types/<int:type_id>', methods=['PUT'])
def update_parcel_type(type_id):
    """Update an existing parcel type."""
    parcel_type = next((t for t in parcel_types if t["id"] == type_id), None)
    if parcel_type:
        data = request.json
        parcel_type["name"] = data.get("name", parcel_type["name"])
        return jsonify(parcel_type)
    return jsonify({"error": "Parcel type not found"}), 404

@app.route('/parcel_types/<int:type_id>', methods=['DELETE'])
def delete_parcel_type(type_id):
    """Delete a parcel type."""
    global parcel_types
    parcel_types = [t for t in parcel_types if t["id"] != type_id]
    return jsonify({"message": "Parcel type deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
