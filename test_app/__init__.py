from flask import Flask
from test_app.routes.controller import bp
from test_app.models import db
from test_app.models import Data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testData.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(bp)

with app.app_context():
    db.create_all()