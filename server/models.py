# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password_hash = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     parcels = db.relationship('Parcel', backref='user', lazy=True)
#     notifications = db.relationship('Notification', backref='user', lazy=True)

# class Parcel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=True)
#     weight = db.Column(db.Float, nullable=False)
#     pickup_address = db.Column(db.String(255), nullable=False)
#     pickup_lat = db.Column(db.Float, nullable=False)
#     pickup_lng = db.Column(db.Float, nullable=False)
#     destination_address = db.Column(db.String(255), nullable=False)
#     destination_lat = db.Column(db.Float, nullable=False)
#     destination_lng = db.Column(db.Float, nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     present_location = db.Column(db.String(255), nullable=False)
#     present_location_lat = db.Column(db.Float, nullable=False)
#     present_location_lng = db.Column(db.Float, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     delivery_history = db.relationship('DeliveryHistory', backref='parcel', lazy=True)
#     notifications = db.relationship('Notification', backref='parcel', lazy=True)

# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password_hash = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# class DeliveryHistory(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     location = db.Column(db.String(255), nullable=False)
#     location_lat = db.Column(db.Float, nullable=False)
#     location_lng = db.Column(db.Float, nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# class Notification(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
#     message = db.Column(db.String(255), nullable=False)
#     sent_at = db.Column(db.DateTime, default=datetime.utcnow)

# class ParcelType(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type_name = db.Column(db.String(255), nullable=False)
#     weight_range = db.Column(db.Float, nullable=False)
#     price = db.Column(db.Integer, nullable=False)

# class Driver(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     phone_number = db.Column(db.String(10), nullable=False, unique=True)
    
#     parcels = db.relationship('Parcel', backref='driver', lazy=True)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    parcels = db.relationship('Parcel', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)

class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=True)
    weight = db.Column(db.Float, nullable=False)
    pickup_address = db.Column(db.String(255), nullable=False)
    pickup_lat = db.Column(db.Float, nullable=False)
    pickup_lng = db.Column(db.Float, nullable=False)
    destination_address = db.Column(db.String(255), nullable=False)
    destination_lat = db.Column(db.Float, nullable=False)
    destination_lng = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    present_location = db.Column(db.String(255), nullable=False)
    present_location_lat = db.Column(db.Float, nullable=False)
    present_location_lng = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    delivery_history = db.relationship('DeliveryHistory', backref='parcel', lazy=True)
    notifications = db.relationship('Notification', backref='parcel', lazy=True)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DeliveryHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    location_lat = db.Column(db.Float, nullable=False)
    location_lng = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

class ParcelType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=False)
    weight_range = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)
    
    parcels = db.relationship('Parcel', backref='driver', lazy=True)
