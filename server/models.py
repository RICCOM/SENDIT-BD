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
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #Relationships
    parcels = db.relationship('Parcel', back_populates='users', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='users', cascade='all, delete-orphan')

    #Serialization_rules
    serialize_rules = ('-parcels.user', '-notifications.user')

class Parcel(db.Model, SerializerMixin):
    __tablename__ = 'parcels'

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

    #Relationships
    user = db.relationship('User', back_populates='parcels')
    driver = db.relationship('Driver', back_populates='parcels')
    delivery_history = db.relationship('DeliveryHistory', back_populates='parcels', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='parcels', cascade='all, delete-orphan')

    #Serialization rules
    serialize_rules = ('-users.parcel', '-drivers.parcel', '-delivery_histories.parcel', 'notifications.parcel')

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DeliveryHistory(db.Model, SerializerMixin):
    __tablename__ = 'delivery_histories'

    id = db.Column(db.Integer, primary_key=True)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    location_lat = db.Column(db.Float, nullable=False)
    location_lng = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #Relationships
    parcel = db.relationship('Parcel', back_populates='delivery_histories')

    #Serialization rules
    serialize_rules = ('-parcels.delivery_history')

class Notification(db.Model, SerializerMixin):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcel.id'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    #Relationships
    user = db.relationship('User', back_populates='notifications')
    parcel = db.relationship('Parcel', back_populates='notifications')

    #Serialization rules
    serialize_rules = ('-users.notification', '-parcels.notification')

class ParcelType(db.Model, SerializerMixin): 
    __tablename__ = 'parcel_types'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=False)
    weight_range = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Driver(db.Model, SerializerMixin):
    ___tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)

    #Relationships
    parcels = db.relationship('Parcel', back_populates='drivers')

    #Serialization rules
    serialize_rules = ('-parcels.driver')

