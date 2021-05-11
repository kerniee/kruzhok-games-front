from flask import (
    Blueprint, redirect, session, url_for
)

# from app.database import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
