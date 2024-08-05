from flask import Flask, jsonify, request

app = Flask(__name__)


parcels = [
    {"id": 1, "name": "Parcel 1", "type": "Type A", "weight": 10.5},
    {"id": 2, "name": "Parcel 2", "type": "Type B", "weight": 5.0},
]

@app.route('/parcels', methods=['GET'])
def get_parcels():
    """Get all parcels."""
    return jsonify(parcels)

@app.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    """Get a specific parcel by ID."""
    parcel = next((p for p in parcels if p["id"] == parcel_id), None)
    if parcel:
        return jsonify(parcel)
    return jsonify({"error": "Parcel not found"}), 404

@app.route('/parcels', methods=['POST'])
def create_parcel():
    """Create a new parcel."""
    data = request.json
    new_parcel = {
        "id": len(parcels) + 1,
        "name": data.get("name"),
        "type": data.get("type"),
        "weight": data.get("weight")
    }
    parcels.append(new_parcel)
    return jsonify(new_parcel), 201

@app.route('/parcels/<int:parcel_id>', methods=['PUT'])
def update_parcel(parcel_id):
    """Update an existing parcel."""
    parcel = next((p for p in parcels if p["id"] == parcel_id), None)
    if parcel:
        data = request.json
        parcel["name"] = data.get("name", parcel["name"])
        parcel["type"] = data.get("type", parcel["type"])
        parcel["weight"] = data.get("weight", parcel["weight"])
        return jsonify(parcel)
    return jsonify({"error": "Parcel not found"}), 404

@app.route('/parcels/<int:parcel_id>', methods=['DELETE'])
def delete_parcel(parcel_id):
    """Delete a parcel."""
    global parcels
    parcels = [p for p in parcels if p["id"] != parcel_id]
    return jsonify({"message": "Parcel deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
