from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])