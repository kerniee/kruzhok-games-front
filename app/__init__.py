import os

from decouple import config
from flask import Flask

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
# gunicorn_logger = logging.getLogger('gunicorn.error')
# app.logger.handlers = gunicorn_logger.handlers
app.config['SECRET_KEY'] = SECRET_KEY

from app.views.all import *
from app.views import auth

app.register_blueprint(auth.auth_bp)

if __name__ == '__main__':
    app.debug = config("DEBUG", cast=bool, default=False)
    app.run("0.0.0.0", port=8000)
