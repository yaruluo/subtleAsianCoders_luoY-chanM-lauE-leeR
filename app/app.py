# from app.utl import build_db
from flask import Flask, render_template, flash, redirect, url_for, request, session
from utl import models
from utl.config import Config
import os

# SQLAlchemy DB Models
db = models.db
Songs = models.Songs
Albums = models.Albums
Lyrics = models.Lyrics
Listens = models.Listens
AlbumCoverArts = models.AlbumCoverArts
SingleCoverArts = models.SingleCoverArts

app = Flask(__name__)
app.config.from_object(Config)

#creates secret key for sessions
app.secret_key = os.urandom(32)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
