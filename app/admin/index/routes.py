from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, logout_user, login_user
from .forms import LoginForm

from app import bcrypt
from ..users.models import Users


land_admin = Blueprint('land_admin', __name__)


# # Landing page
@land_admin.route('/')
@login_required
def landing():
    title = "Skidrow games download"
    return render_template('./admin/pages/index.html', title = title)


# Login
@land_admin.route('/login', methods = ['POST', 'GET'])
def login():
    title = "Login to website"
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username = username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash(f"Welcome back {username}!", "success")
            return redirect(request.args.get('next') or url_for('land_admin.landing'))
        else: flash("Something went wrong", "danger")
        
    return render_template('./admin/pages/login.html', title = title, form = form)


# Logout
@land_admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Goodbye!", "success")
    return redirect(url_for("land_admin.landing"))