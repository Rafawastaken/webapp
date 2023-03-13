from flask import Blueprint, request, render_template, url_for, flash, redirect
from flask_login import login_required

from app import db
from .forms import AddGameForm, AddGenreForm
from .models import Game, Genre

# Blueprint
games_admin = Blueprint('games_admin', __name__)

###### * Games * ######

# List all games
@games_admin.route('/')
@login_required
def games_list():
    games = Game.query.all()
    return render_template('./admin/pages/games/games.html')


# Add games
@games_admin.route('/add-game', methods = ['POST', 'GET'])
def add_game():
    title = "Add Games to Website"
    form = AddGameForm()
    genres = Genre.query.all()

    if form.validate_on_submit():
        genre_selected = request.form.get('genre')
 
        new_game = Game(
            game_id = form.game_id.data,
            name = form.name.data,
            release_data = form.release_data.data,
            rating = form.rating.data,
            genre_id = genre_selected,
            bg_image = form.image.data,
            download_link = form.download_link.data,
        )

        db.session.add(new_game)
        db.session.commit()

        flash("Game added with successfully!", "success")
        return redirect(url_for('games_admin.games_list'))
    return render_template('./admin/pages/games/add_game.html', title = title, form = form, genres = genres)



###### * Genres * ######

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

# Delete genre
@games_admin.route('/delete-genre/<int:id>', methods = ['POST'])
@login_required
def delete_genre(id):
    genre_delete = Genre.query.filter_by(id = id).first()
    db.session.delete(genre_delete)
    db.session.commit()
    flash("Genre was deleted!", "success")
    return redirect(url_for('games_admin.genres'))

