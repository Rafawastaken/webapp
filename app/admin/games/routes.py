from flask import Blueprint, request, render_template, url_for, flash

from .models import Game, Genre

# Blueprint
games_admin = Blueprint('games_admin', __name__)

###### * Game Management * ######

# List all games
@games_admin.route('/')
def games_list():
    games = Game.query.all()
    return render_template('./admin/pages/games/games.html')