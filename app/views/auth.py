from flask import (
    Blueprint, redirect, session, url_for, request, flash, render_template
)

from flask_login import login_required, logout_user, login_user
from werkzeug.security import check_password_hash

from app import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
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
