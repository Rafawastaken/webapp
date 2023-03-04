from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import RegisterForm, LoginForm
from .models import Games, Users

from app import app, db, bcrypt
from flask_login import login_required, login_user, logout_user, current_user

# Blueprint
admin = Blueprint('admin', __name__)


###### * Admin routes * ######

# Landing page
@admin.route('/')
@login_required
def admin_landing():
    title = "Skidrow games download"
    return render_template('./admin/pages/index.html', title = title)



###### * User management * ######

# Users
@admin.route('/users', methods = ['POST', 'GET'])
def users():
    users = Users.query.all()
    return render_template('./admin/pages/users.html', users = users)


# Add users
@admin.route('/add-user', methods = ['POST', 'GET'])
@login_required
def register():
    form = RegisterForm()            
    title = "Register new user"

    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        new_user = Users(
            username = form.username.data,
            password = hash_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash(f"User: {form.username.data} was added!", 'success')
        return redirect(url_for('admin.users'))

    return render_template('./admin/pages/register.html', form = form, title = title)


# Edit User
@admin.route('/edit-user/<int:id>', methods = ['POST', 'GET'])
@login_required
def edit_user(id):
    ...

# Delete User
@admin.route('/admin/delete-user/<int:id>', methods = ['POST'])
def delete_user(id):
    user_delete = Users.query.filter_by(id = id).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash(f"{user_delete.username} was deleted from website", 'success')
    return redirect(url_for('admin.users'))

###### * Session Manager * ######


# Login
@admin.route('/login', methods = ['POST', 'GET'])
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
            return redirect(request.args.get('next') or url_for('admin.admin_landing'))
        else: 
            flash("Something went wrong", "danger")


    return render_template('./admin/pages/login.html', title = title, form = form)


# Logout
@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Goodbye!", "success")
    return redirect(url_for("admin.admin_landing"))