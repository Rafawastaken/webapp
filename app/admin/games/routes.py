from flask import Blueprint, request, render_template, url_for, flash, redirect
from flask_login import login_required

from app import db
from .forms import AddGenreForm
from .models import Game, Genre

# Blueprint
games_admin = Blueprint('games_admin', __name__)

###### * Game Management * ######

# List all games
@games_admin.route('/')
@login_required
def games_list():
    games = Game.query.all()
    return render_template('./admin/pages/games/games.html')


# Add/View Genres
@games_admin.route('/add-genre', methods = ['POST', 'GET'])
@login_required
def genres():
    title = "View Games Genres"
    form = AddGenreForm()
    genres = Genre.query.all()

    # Add genre if form is submited
    if form.validate_on_submit():
        new_genre = Genre(name = form.genre.data)
        db.session.add(new_genre)
        db.session.commit()
        flash(f"Genre: {form.genre.data} added successfully!", 'success')
        return redirect(request.referrer or url_for('games_admin.genres'))


    return render_template('./admin/pages/games/genres.html', form = form, title = title, genres = genres)

# Delte genre
@games_admin.route('/delete-genre/<int:id>', methods = ['POST'])
@login_required
def delete_genre(id):
    genre_delete = Genre.query.filter_by(id = id).first()
    db.session.delete(genre_delete)
    db.session.commit()
    flash("Genre was deleted!", "success")
    return redirect(url_for('games_admin.genres'))

# Add games
@games_admin.route('/add-game', methods = ['POST', 'GET'])
@login_required
def add_game():
    ...
