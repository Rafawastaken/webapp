from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import RegisterForm, LoginForm
from .models import Users

from app import app, db, bcrypt
from flask_login import login_required, login_user, logout_user, current_user

# Blueprint
users_admin = Blueprint('admin', __name__)

###### * User management * ######

# Users
@users_admin.route('/users', methods = ['POST', 'GET'])
def users():
    users = Users.query.all()
    return render_template('./admin/pages/users/users.html', users = users)


# Add users
@users_admin.route('/add-user', methods = ['POST', 'GET'])
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

    return render_template('./admin/pages/users/register.html', form = form, title = title)


# Edit User
@users_admin.route('/edit-user/<int:id>', methods = ['POST', 'GET'])
@login_required
def edit_user(id):
    form = RegisterForm()
    user = Users.query.filter_by(id = id).first()
    title = f"Edit {user.username} profile"

    if form.validate_on_submit():
        user.username = form.username.data
        user.password = bcrypt.generate_password_hash(form.password.data)
        db.session.commit()

        flash(f"{user.username} updated successfully!", "success")
        return redirect(url_for('admin.users'))


    return render_template('./admin/pages/users/edit.html', user = user, form = form)

# Delete User
@users_admin.route('/admin/delete-user/<int:id>', methods = ['POST'])
def delete_user(id):
    user_delete = Users.query.filter_by(id = id).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash(f"{user_delete.username} was deleted from website", 'success')
    return redirect(url_for('admin.users'))
