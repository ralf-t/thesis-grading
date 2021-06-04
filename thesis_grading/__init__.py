from flask import Flask
from thesis_grading.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from thesis_grading.main.routes import main
    from thesis_grading.thesis.routes import thesis
    from thesis_grading.user.routes import user
    # from thesis_grading.group.routes import group
    
    app.register_blueprint(main)
    app.register_blueprint(thesis)
    app.register_blueprint(user)
    # app.register_blueprint(group)
    

    return app