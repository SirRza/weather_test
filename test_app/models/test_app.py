from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(200), nullable=False)



class Redis():
    def __init__(self ,id, user_id, location, time):
        self.id = id
        self.user_id = user_id
        self.location = location
        self.time = time

    
    def to_redis(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'location': self.location,
            'time': self.time
        }
