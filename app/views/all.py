import os
from collections import defaultdict

from flask import render_template, redirect, url_for, flash, send_from_directory
from flask_login import current_user, login_required

from app.crud import *
from app.models import *

from app import app, login_manager

GAMES = ("dota2", "overwatch", "csgo")


def unauthorized():
    flash("Для доступа к странице требуется авторизация")
    return redirect(url_for('auth.login'))


login_manager.unauthorized = unauthorized


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template("index.html", games=Game.query.all())


@app.route('/games/<game_name>')
@login_required
def games(game_name):
    game = get_game_by_url(game_name)
    if game is not None:
        return render_template(f"game.html", game=game, games=Game.query.all())


@app.route("/profile")
@login_required
def profile():
    me = defaultdict(lambda e: "Не указано", current_user.get_me())

    groups = [
        {
            "name": "Личные данные",
            "ФИО": me["last_name"] + " " + me["first_name"] + " " + me["middle_name"],
            "Дата рождения": me["birthday"],
            "Пол": "Мужской" if me["sex"] == 'm' else "Женский",
            "Адрес": me["address"]
        },
        {
            "name": "О себе",
            "О себе": me["about"]
        }
    ]

    return render_template("profile.html", groups=groups)


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/check-level")
@login_required
def check_level():
    return render_template("check_level.html", games=Game.query.all())
