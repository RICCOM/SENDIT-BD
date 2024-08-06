from flask import Flask
from models import db, User, Parcel, Admin, DeliveryHistory, Notification,ParcelType,Driver
from flask_migrate import Migrate



from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity,current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "b'Y\xf1Xz\x01\xad|eQ\x80t \xca\x1a\x10K'"  
app.config['JWT_TOKEN_LOCATION'] = ['headers']
jwt = JWTManager(app)
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()



app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "SENDIT!"

if __name__ == '__main__':
    app.run(debug=True)

