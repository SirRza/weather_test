from datetime import datetime
from .app import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    location = db.Column(db.String(100), nullable=False)
    redis = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.Integer, nullable=False)