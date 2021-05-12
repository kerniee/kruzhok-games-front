import pickle

from authlib.integrations.requests_client import OAuth2Session

from models import *
from app import db


def get_game_by_url(url_name: str):
    game = Game.query.filter_by(url_name=url_name).first()
    return game


def get_me(user: User):
    client = OAuth2Session(user.username, user.password, token=pickle.loads(user.token))
    resp = client.get('https://talent.kruzhok.org/api/users/me')
    if resp.status_code == 200:
        data = resp.json()
        return data
