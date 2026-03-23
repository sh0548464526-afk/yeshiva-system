
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tz = db.Column(db.String(20))
    name = db.Column(db.String(100))

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    active = db.Column(db.Boolean)

class Seder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    start = db.Column(db.String(5))
    amount = db.Column(db.Float)
    late = db.Column(db.Float)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tz = db.Column(db.String(20))
    day = db.Column(db.String(20))
    s1 = db.Column(db.String(5))
    s2 = db.Column(db.String(5))
    s3 = db.Column(db.String(5))
