from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators, ValidationError
from .models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min = 4, max = 20), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), 
                                          validators.EqualTo('password_repeat', message = 'Passwords dont match')])
    password_repeat = PasswordField('Repeat Password')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])