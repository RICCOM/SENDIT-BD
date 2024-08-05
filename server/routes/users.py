
from flask import Flask, jsonify, request

app = Flask(_name_)

# Dummy data for users
users = [
    {"id": 1, "username": "user1", "email": "user1@example.com", "role": "user"},
    {"id": 2, "username": "user2", "email": "user2@example.com", "role": "user"},
]

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "username": data.get("username"),
        "email": data.get("email"),
        "role": data.get("role", "user")
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        data = request.json
        user["username"] = data.get("username", user["username"])
        user["email"] = data.get("email", user["email"])
        user["role"] = data.get("role", user["role"])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 204

if __name__ == "_main_":
    app.run(debug=True)