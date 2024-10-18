from flask import Flask
from config import Config
from db import db
from utils import celery_init_app


def create_app(database_uri='sqlite:///task_management.db'):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    db.init_app(app)
    celery = celery_init_app(app)
    with app.app_context():
        db.create_all()

    return app, celery