from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/sendit_db'
db = SQLAlchemy(app)

class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Other parcel fields
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(50))
    destination = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    # Other user fields

@app.route('/user/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    # Other user data
    user = User(email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    # Authentication logic
    return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/user/create_parcel', methods=['POST'])
def create_parcel():
    data = request.get_json()
    user_id = data.get('user_id')
    # Other parcel data
    parcel = Parcel(user_id=user_id)
    db.session.add(parcel)
    db.session.commit()
    return jsonify({'message': 'Parcel created successfully'}), 201

@app.route('/user/change_destination/<int:parcel_id>', methods=['PUT'])
def change_destination(parcel_id):
    data = request.get_json()
    new_destination = data.get('new_destination')
    parcel = Parcel.query.get(parcel_id)
    if parcel and parcel.status != 'delivered':
        parcel.destination = new_destination
        db.session.commit()
        return jsonify({'message': 'Destination updated successfully'}), 200
    return jsonify({'message': 'Parcel not found or already delivered'}), 404

@app.route('/user/cancel_parcel/<int:parcel_id>', methods=['PUT'])
def cancel_parcel(parcel_id):
    parcel = Parcel.query.get(parcel_id)
    if parcel and parcel.status != 'delivered':
        parcel.status = 'cancelled'
        db.session.commit()
        return jsonify({'message': 'Parcel cancelled successfully'}), 200
    return jsonify({'message': 'Parcel not found or already delivered'}), 404

@app.route('/user/view_parcel/<int:parcel_id>', methods=['GET'])
def view_parcel(parcel_id):
    parcel = Parcel.query.get(parcel_id)
    if parcel:
        return jsonify({
            'id': parcel.id,
            'status': parcel.status,
            'current_location': parcel.current_location,
            'destination': parcel.destination
            # Other parcel details
        }), 200
    return jsonify({'message': 'Parcel not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
