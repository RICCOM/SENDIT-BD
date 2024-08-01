from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity, jwt_required
)
import os
from config import db, app
from models import User, Parcel, Admin, DeliveryHistory, Notification, ParcelType, Driver
jwt = JWTManager(app)
api = Api(app)

class Home(Resource):
    def get(self):
        return {"message": "Welcome to SendIT!"}

api.add_resource(Home, '/')


