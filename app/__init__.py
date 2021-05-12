import os

from decouple import config
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
# gunicorn_logger = logging.getLogger('gunicorn.error')
# app.logger.handlers = gunicorn_logger.handlers
app.config['SECRET_KEY'] = SECRET_KEY

DB_URI = config("DB_URI", default='sqlite:///db.sqlite3')
DEBUG = config("DEBUG", default=False, cast=bool)
REDIRECT_URI = config("REDIRECT_URI", default="http://localhost:8080/api/return")
AUTHORIZATION_ENDPOINT = config("AUTHORIZATION_ENDPOINT", default="https://talent.kruzhok.org/oauth/authorize/")
TOKEN_ENDPOINT = config("TOKEN_ENDPOINT", default="https://talent.kruzhok.org/api/oauth/issue-token/")

app.debug = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app.views.all import *
from app.views import auth

app.register_blueprint(auth.auth_bp)

if __name__ == '__main__':
    app.debug = config("DEBUG", cast=bool, default=False)
    app.run("0.0.0.0", port=8000)
