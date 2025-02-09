from datetime import datetime
from . import db

class URLShortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2083), nullable=False, unique=True)
    shortened_url = db.Column(db.String(100), nullable=False, unique=True)
    creation_date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Shortened URL ID %r>' %self.id