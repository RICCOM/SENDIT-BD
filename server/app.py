from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "SENDIT!"

if __name__ == '__main__':
    app.run(debug=True)

