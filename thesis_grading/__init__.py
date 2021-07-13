from flask import Flask
from flask_wtf.csrf import CSRFProtect
from thesis_grading.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# extensions
csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from thesis_grading.main.routes import main
    from thesis_grading.thesis.routes import thesis
    from thesis_grading.user.routes import user
    # from thesis_grading.group.routes import group
    
    app.register_blueprint(main)
    app.register_blueprint(thesis)
    app.register_blueprint(user)
    # app.register_blueprint(group)
    
    # import models for flask migrate
    import thesis_grading.models 

    return app