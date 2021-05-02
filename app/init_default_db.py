from app.models import *
from app.database import *
import json
import random


init_db()
u = User(name="admin", password="admin")
db_session.add(u)
db_session.commit()
