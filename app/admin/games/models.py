from app import db
from datetime import datetime

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Game(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    
    game_id = db.Column(db.String(50),unique=False, nullable=True)
    name = db.Column(db.String(50),unique=False, nullable=False)
    release_data = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(15), unique=True, nullable=True)
    
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('game', lazy=True))
    
    bg_image = db.Column(db.String(380),unique=False, nullable=False)
    download_link = db.Column(db.String(380),unique=False, nullable=False)

    added = db.Column(db.String(20), unique = False, nullable = True, default = str(datetime.now()).split('.')[0])
