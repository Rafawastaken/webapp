from flask import Blueprint


games_admin = Blueprint('games', __name__)

@games_admin.route('/')
def games_list():
    return "games"