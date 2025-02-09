from flask import Flask
from app.routes.home_route import home_bp
from app.routes.swagger_route import swagger_bp
from app.routes.url_route import url_bp
from .config import Config
from app.instance.db_models import db
from tools.utils import celery_init_app
from os import getenv


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    celery = celery_init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(swagger_bp, url_prefix=getenv('SWAGGER_URL'))
    app.register_blueprint(home_bp,template_folder='/templates')
    app.register_blueprint(url_bp, template_folder='/templates')
    return app, celery