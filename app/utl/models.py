from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Song(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    inalbum = db.Column(db.Integer, nullable=False)

class Album(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    aid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)

class Lyric(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    lyric = db.Column(db.Text, nullable=False)

class Listen(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    numlisten = db.Column(db.Integer, nullable=False)

class AlbumCoverArt(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    coverartlink = db.Column(db.Text, nullable=False)

class SingleCoverArt(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    coverartlink = db.Column(db.Text, nullable=False)
