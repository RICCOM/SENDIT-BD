from flask import Flask, jsonify, request

app = Flask(_name_)

# Dummy data for admin actions
admin_actions = [
    {"id": 1, "action": "User created", "details": "user1 was created"},
    {"id": 2, "action": "User deleted", "details": "user2 was deleted"},
]

@app.route('/admin/actions', methods=['GET'])
def get_admin_actions():
    """Get all admin actions."""
    return jsonify(admin_actions)

@app.route('/admin/actions/<int:action_id>', methods=['GET'])
def get_admin_action(action_id):
    """Get a specific admin action by ID."""
    action = next((a for a in admin_actions if a["id"] == action_id), None)
    if action:
        return jsonify(action)
    return jsonify({"error": "Action not found"}), 404

@app.route('/admin/actions', methods=['POST'])
def create_admin_action():
    """Create a new admin action."""
    data = request.json
    new_action = {
        "id": len(admin_actions) + 1,
        "action": data.get("action"),
        "details": data.get("details")
    }
    admin_actions.append(new_action)
    return jsonify(new_action), 201

if _name_ == "_main_":
    app.run(debug=True)