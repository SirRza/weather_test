from flask import Flask ,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


appi = Flask(__name__)
appi.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(appi)


with appi.app_context():
    db.create_all()