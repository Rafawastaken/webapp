from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(180),unique=False, nullable=False)
    creation_date = db.Column(db.String(20), unique = False, nullable = True, default = str(datetime.now()).split('.')[0])


class Games(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(50),unique=False, nullable=True)
    name = db.Column(db.String(50),unique=False, nullable=False)

    release_data = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(15), unique=True, nullable=True)
    genres = db.Column(db.String(180),unique=False, nullable=False)
    bg_image = db.Column(db.String(380),unique=False, nullable=False)
    download_link = db.Column(db.String(380),unique=False, nullable=False)

