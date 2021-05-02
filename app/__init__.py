from flask import Flask

import logging
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.config['SECRET_KEY'] = SECRET_KEY

from app.views import *
