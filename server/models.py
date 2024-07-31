from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db, bcrypt
from datetime import datetime
import re

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    #Relationships
    parcels = db.relationship("Parcel", back_populates="user")
    notifications = db.relationship("Notification", back_populates="user")

    #Serialization rules
    serialize_rules = ('-parcels.user', '-notifications.user')

class Parcel(db.Model, SerializerMixin):
    __tablename__ = 'parcels'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
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
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    #Relationships
    user = db.relationship("User", back_populates="parcels")
    delivery_histories = db.relationship("DeliveryHistory", back_populates="parcels")
    notifications = db.relationship("Notification", back_populates="parcels")
    drivers = db.relationship("Driver", back_populates="parcels")

    #Serialization rules
    serialize_rules = ('-users.parcel', '-delivery_histories.parcel', '-notifications.parcel', '-drivers.parcel')

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class DeliveryHistory(db.Model, SerializerMixin):
    __tablename__ = 'delivery_histories'

    id = db.Column(db.Integer, primary_key=True)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcels.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    location_lat = db.Column(db.Float, nullable=False)
    location_lng = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    #Relationships
    parcel = db.relationship("Parcel", back_populates="delivery_histories")

    # Serialization rules
    serialize_rules = ('-parcels.delivery_history')

class Notification(db.Model, SerializerMixin):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    parcel_id = db.Column(db.Integer, db.ForeignKey('parcels.id'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    sent_at = db.Column(db.DateTime, nullable=False)

    #Relationships
    user = db.relationship("User", back_populates="notifications")
    parcel = db.relationship("Parcel", back_populates="notifications")

    # Serialization rules
    serialize_rules = ('-users.notification', '-parcels.notification')

class ParcelType(db.Model, SerializerMixin):
    __tablename__ = 'parcel_types'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=False)
    weight_range = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Driver(db.Model, SerializerMixin):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.COlumn(db.String(255), nullable=False)
    phone_number = db.COlumn(db.Integer(10), nullable=False)

    #Relationships
    parcels = db.relationship("Parcel", back_populates="drivers")    

    #Serialization rules
    serialize_rules = ('-parcels.driver')