from flask_wtf import FlaskForm
from wtforms import StringField, validators

# Form to add games
class AddGameForm(FlaskForm):
    name = StringField('Game Name', [validators.DataRequired()])
    game_id = StringField('Game ID')
    rating = StringField('Rating', [validators.DataRequired()])
    image = StringField('image', [validators.DataRequired()])
    release_data = StringField('Release Date', [validators.DataRequired()])
    download_link = StringField('Download Link')

# Form to add genres
class AddGenreForm(FlaskForm):
    genre = StringField('Genre', [validators.Length(min = 4, max = 25), validators.DataRequired()])