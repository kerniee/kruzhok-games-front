import pickle

from flask import (
    Blueprint, redirect, session, url_for, request, flash, render_template
)

from flask_login import login_required, logout_user, login_user
from werkzeug.security import check_password_hash
from authlib.integrations.requests_client import OAuth2Session

from app import User, REDIRECT_URI, AUTHORIZATION_ENDPOINT, TOKEN_ENDPOINT, db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def get_auth_token(username: str, password: str):
    client = OAuth2Session(username, password, token_endpoint_auth_method='client_secret_post')
    token = client.fetch_token(TOKEN_ENDPOINT, username=username, password=password, grant_type='password')
    return token


@auth_bp.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    token = get_auth_token(email, password)

    if "non_field_errors" in token:
        flash(token['non_field_errors'])
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(username=email).first()
    if user is None:
        user = User(username=email, password=password)

    user.token = pickle.dumps(token)
    with db.session.no_autoflush:
        db.session.add(user)
        db.session.commit()


    login_user(user, remember=remember)

    return redirect(url_for('index'))


@auth_bp.route('/login', methods=["GET"])
def login():
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('index'))
