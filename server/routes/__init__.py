from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sendit.db'  # Example database URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    

    with app.app_context():
        from . import users, admins, notifications, drivers, parcel_types, parcels, delivery_history
        app.register_blueprint(users.bp)
        app.register_blueprint(admins.bp)
        app.register_blueprint(notifications.bp)
        app.register_blueprint(drivers.bp)
        app.register_blueprint(parcel_types.bp)
        app.register_blueprint(parcels.bp)
        app.register_blueprint(delivery_history.bp)

        db.create_all()  # Create tables

    return app