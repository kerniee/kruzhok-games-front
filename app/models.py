from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float
from flask_login import UserMixin
from app import db
from sqlalchemy.orm import relationship


db.metadata.clear()


class Game(db.Model):
    __tablename__ = 'games'
    __extend_existing__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url_name = Column(String)
    images_path = Column(String)

    def __repr__(self):
        return '<Game %r>' % self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
