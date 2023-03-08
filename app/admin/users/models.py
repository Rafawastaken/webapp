from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(180),unique=False, nullable=False)
    creation_date = db.Column(db.String(20), unique = False, nullable = True, default = str(datetime.now()).split('.')[0])



