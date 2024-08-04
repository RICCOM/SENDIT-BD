import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Change to your preferred database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
