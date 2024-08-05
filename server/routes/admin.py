from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/sendit_db'
db = SQLAlchemy(app)
mail = Mail(app)

class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Other parcel fields
    status = db.Column(db.String(50))
    current_location = db.Column(db.String(100))
    destination = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    # Other user fields

@app.route('/admin/change_status/<int:parcel_id>', methods=['PUT'])
def change_status(parcel_id):
    data = request.get_json()
    status = data.get('status')
    parcel = Parcel.query.get(parcel_id)
    if parcel:
        parcel.status = status
        db.session.commit()
        # Notify user
        user = User.query.get(parcel.user_id)
        send_email(user.email, 'Parcel Status Update', f'Your parcel status has been updated to {status}.')
        return jsonify({'message': 'Status updated successfully'}), 200
    return jsonify({'message': 'Parcel not found'}), 404

@app.route('/admin/change_location/<int:parcel_id>', methods=['PUT'])
def change_location(parcel_id):
    data = request.get_json()
    current_location = data.get('current_location')
    parcel = Parcel.query.get(parcel_id)
    if parcel:
        parcel.current_location = current_location
        db.session.commit()
        # Notify user
        user = User.query.get(parcel.user_id)
        send_email(user.email, 'Parcel Location Update', f'Your parcel is now at {current_location}.')
        return jsonify({'message': 'Location updated successfully'}), 200
    return jsonify({'message': 'Parcel not found'}), 404

def send_email(to, subject, body):
    msg = Message(subject, recipients=[to])
    msg.body = body
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
