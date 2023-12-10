from . import db
from flask_login import UserMixin
from datetime import datetime

# define User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    car = db.relationship('Car')
    

# define Note Model
class Car(db.Model):
    car_number = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


