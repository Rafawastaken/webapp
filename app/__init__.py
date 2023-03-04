from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy()

with app.app_context():
    # Config file
    app.config.from_pyfile("config.py")

    # Init database
    db.init_app(app)

    # Encrypt
    bcrypt = Bcrypt(app)

    # Login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    login_manager.login_message_category = 'danger'
    login_manager.needs_refresh_message_category ='danger'
    login_manager.login_message = u'You need to be logged in'

    # Migrations
    migrate = Migrate(app, db)
    
    #### Routes #### 
    from .admin.routes import admin
    from .public.routes import public

    app.register_blueprint(admin, url_prefix = '/admin')
    app.register_blueprint(public, url_prefix = '/')