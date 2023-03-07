from app import db

class Games(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(50),unique=False, nullable=True)
    name = db.Column(db.String(50),unique=False, nullable=False)

    release_data = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(15), unique=True, nullable=True)
    genres = db.Column(db.String(180),unique=False, nullable=False)
    bg_image = db.Column(db.String(380),unique=False, nullable=False)
    download_link = db.Column(db.String(380),unique=False, nullable=False)
