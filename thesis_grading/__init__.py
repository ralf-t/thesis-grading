from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

from thesis_grading.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf.init_app(app)

    from thesis_grading.main.routes import main
    from thesis_grading.thesis.routes import thesis
    from thesis_grading.user.routes import user
    from thesis_grading.dashboard.routes import dashboard
    # from thesis_grading.group.routes import group
    
    app.register_blueprint(main)
    app.register_blueprint(thesis)
    app.register_blueprint(user)
    app.register_blueprint(dashboard)
    # app.register_blueprint(group)
    

    return app