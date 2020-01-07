'''
subtleAsianCoders - Yaru Luo, Matthew Chan, Eric "Morty" Lau, ray. lee.
SoftDev1 pd1
P02 -- RYthEM
'''

# from app.utl import build_db
from flask import Flask, request, redirect, session, render_template, url_for, flash
from utl import models
from config import Config
import sqlite3
import urllib.request
import urllib.parse
import functools
import os
import json
import datetime

# SQLAlchemy DB Models
db = models.db
Song = models.Song
Album = models.Album

app = Flask(__name__)
app.config.from_object(Config)

# creates secret key for sessions
app.secret_key = os.urandom(32)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
