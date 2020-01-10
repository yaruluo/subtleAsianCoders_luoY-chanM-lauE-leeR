from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    aid = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    lyrics = db.Column(db.Text, nullable=False)
    numListen = db.Column(db.Integer, nullable=False)

class Album(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    coverartlink = db.Column(db.Text, nullable=False)
