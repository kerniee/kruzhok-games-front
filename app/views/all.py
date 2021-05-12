from flask import render_template
from flask_login import current_user, login_required

from app.crud import *
from app.models import *

from app import app, login_manager

GAMES = ("dota2", "overwatch", "csgo")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    return render_template("index.html", games=Game.query.all())


@app.route('/games/<game_name>')
def games(game_name):
    game = get_game_by_url(game_name)
    if game is not None:
        return render_template(f"game.html", game=game, games=Game.query.all())


@app.route("/profile")
@login_required
def profile():
    me = get_me(current_user)
    return render_template("profile.html", my_data=me)


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/check-level")
def check_level():
    return render_template("check_level.html")
