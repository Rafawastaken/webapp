from flask_wtf import FlaskForm
from wtforms import StringField, validators

# Form to add games
class AddGameForm(FlaskForm):
    ...

# Form to add genres
class AddGenreForm(FlaskForm):
    genre = StringField('Genre', [validators.Length(min = 4, max = 25), validators.DataRequired()])