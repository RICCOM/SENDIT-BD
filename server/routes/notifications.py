from flask import Flask, jsonify, request

app = Flask(_name_)

# Dummy data for notifications
notifications = [
    {"id": 1, "user_id": 1, "message": "Your order has been shipped.", "status": "unread"},
    {"id": 2, "user_id": 2, "message": "Your account has been verified.", "status": "unread"},
]

@app.route('/notifications', methods=['GET'])
def get_notifications():
    """Get all notifications."""
    return jsonify(notifications)

@app.route('/notifications/<int:notification_id>', methods=['GET'])
def get_notification(notification_id):
    """Get a specific notification by ID."""
    notification = next((n for n in notifications if n["id"] == notification_id), None)
    if notification:
        return jsonify(notification)
    return jsonify({"error": "Notification not found"}), 404

@app.route('/notifications', methods=['POST'])
def create_notification():
    """Create a new notification."""
    data = request.json
    new_notification = {
        "id": len(notifications) + 1,
        "user_id": data.get("user_id"),
        "message": data.get("message"),
        "status": "unread"
    }
    notifications.append(new_notification)
    return jsonify(new_notification), 201

@app.route('/notifications/<int:notification_id>', methods=['PUT'])
def update_notification(notification_id):
    """Update an existing notification."""
    notification = next((n for n in notifications if n["id"] == notification_id), None)
    if notification:
        data = request.json
        notification["status"] = data.get("status", notification["status"])
        return jsonify(notification)
    return jsonify({"error": "Notification not found"}), 404

@app.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    """Delete a notification."""
    global notifications
    notifications = [n for n in notifications if n["id"] != notification_id]
    return jsonify({"message": "Notification deleted"}), 204

if __name__ == "_main_":
    app.run(debug=True)