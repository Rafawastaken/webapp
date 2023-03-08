from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

class Game(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(50),unique=False, nullable=True)
    name = db.Column(db.String(50),unique=False, nullable=False)

    release_data = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(15), unique=True, nullable=True)
    genre = db.relationship('Genre')
    bg_image = db.Column(db.String(380),unique=False, nullable=False)
    download_link = db.Column(db.String(380),unique=False, nullable=False)
