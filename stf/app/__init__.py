import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
mail = Mail()

lm = LoginManager()
lm.session_protection='strong'
lm.login_view='auth.login'

def create_app(config_name):
    """Create an application instance"""
    app = Flask(__name__)

    #Import configuration
    cfg =os.path.join(os.getcwd(),'config',config_name+'.py')
    app.config.from_pyfile(cfg)

    #Initilize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)
    moment.init_app(app)

    #Import Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
