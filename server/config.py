import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

metadata = MetaData()

bcrypt = Bcrypt(app)

CORS(app)