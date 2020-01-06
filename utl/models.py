from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Songs(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    inalbum = db.Column(db.Integer, nullable=False)

class Albums(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    aid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)

class Lyrics(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    lyric = db.Column(db.Text, nullable=False)

class Listens(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    numlisten = db.Column(db.Integer, nullable=False)

class AlbumCoverArts(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    coverartlink = db.Column(db.Text, nullable=False)

class SingleCoverArts(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    coverartlink = db.Column(db.Text, nullable=False)
