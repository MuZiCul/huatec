from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.Integer, default=0)
    join_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now)


class basicModel(db.Model):
    __tablename__ = "basic"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    school = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    zip = db.Column(db.String(200))
    address = db.Column(db.String(200))
    creat_time = db.Column(db.DateTime, default=datetime.now)
