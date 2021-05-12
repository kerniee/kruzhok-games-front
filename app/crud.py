from models import *
from app import db


def get_game_by_url(url_name: str):
    game = Game.query.filter_by(url_name=url_name).first()
    return game
