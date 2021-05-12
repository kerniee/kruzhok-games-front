from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, TypeDecorator
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


class HexByteString(TypeDecorator):
    """Convert Python bytestring to string with hexadecimal digits and back for storage."""

    impl = String

    def process_bind_param(self, value, dialect):
        if not isinstance(value, bytes):
            raise TypeError("HexByteString columns support only bytes values.")
        return value.hex()

    def process_result_value(self, value, dialect):
        return bytes.fromhex(value) if value else None


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=False)
    token = Column(HexByteString(256), unique=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
