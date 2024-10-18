from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class URLShortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String, nullable=False, unique=True)
    shortened_url = db.Column(db.String)
    creation_date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Shortened URL ID %r>' %self.id