import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from db import db

@pytest.fixture
def app():
    app, celery = create_app('sqlite:///:memory:')
    celery.conf.task_always_eager = True

    with app.app_context():
        db.create_all()
    yield app, celery

@pytest.fixture
def client(app):
    app, _ = app
    return app.test_client()
