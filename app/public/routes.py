from flask import Blueprint, render_template

# Blueprint
public = Blueprint('public', __name__)


# Public routes
@public.route('/')
def landing_public():
    return render_template('/public/pages/index.html')