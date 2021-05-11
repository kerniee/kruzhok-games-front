from flask import render_template

from app import app

GAMES = ("dota2", "overwatch", "csgo")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/games/<game_name>')
def games(game_name):
    if game_name in GAMES:
        return render_template(f"{game_name}.html")
