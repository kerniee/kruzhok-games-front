from werkzeug.security import generate_password_hash

from app.models import *
from app import db

db.create_all()
u = User(username="admin", password=generate_password_hash("admin", method='sha256'))
db.session.add(u)

dota2 = Game(name="Dota 2", url_name="dota2", images_path="images/dota2")
csgo = Game(name="CS:GO", url_name="csgo2", images_path="images/csgo")
overwatch = Game(name="Overwatch", url_name="overwatch", images_path="images/overwatch")

db.session.add(dota2)
db.session.add(csgo)
db.session.add(overwatch)
db.session.commit()
