'''
subtleAsianCoders - Yaru Luo, Matthew Chan, Eric "Morty" Lau, ray. lee.
SoftDev1 pd1
P02 -- RYthEM
'''

# from app.utl import build_db
from flask import Flask, request, redirect, session, render_template, url_for, flash
from utl import models
from utl.config import Config
import sqlite3
import urllib.request
import urllib.parse
import functools
import os
import json
from datetime import datetime
import time

# SQLAlchemy DB Models
# db = models.db
# Songs = models.Songs
# Albums = models.Albums
# Lyrics = models.Lyrics
# Listens = models.Listens
# AlbumCoverArts = models.AlbumCoverArts
# SingleCoverArts = models.SingleCoverArts

app = Flask(__name__)
# app.config.from_object(Config)

# creates secret key for sessions
app.secret_key = os.urandom(32)

SPOTIFY_CLIENT_ID = 'b9535e1e2c3741069061954ef75397ab'
SPOTIFY_CLIENT_SECRET = 'bfe2cc0d745b4047ab805445a0ebb25f'
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
SPOTIFY_API_VERSION = 'v1'
SPOTIFY_API_URL = f"{SPOTIFY_API_BASE_URL}/{SPOTIFY_API_VERSION}"

CLIENT_SIDE_URL = 'http://127.0.0.1'
PORT = 5000
SPOTIFY_REDIRECT_URI = f"{CLIENT_SIDE_URL}:{PORT}/callback/q"
SPOTIFY_SCOPE = ''
# SCOPE = 'playlist-modify-public playlist-modify-private'

spotify_auth_query_parameters = {
    'client_id': SPOTIFY_CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': SPOTIFY_REDIRECT_URI,
    'scope': SPOTIFY_SCOPE,
}

@app.route('/')
def root():
    return render_template(
        'home.html',
        # session = session['access_token']
    )

@app.route('/index')
def index():
    authorization_header = {
        'Authorization': f"Bearer {session['access_token']}"
    }
    req = urllib.request.Request(
        "https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V",
        headers=authorization_header,
    )
    print(session['expires_in'])
    req = urllib.request.urlopen(req)
    res = req.read()
    data = json.loads(res)
    return render_template(
        'index.html',
        data = data
    )

@app.route('/spotify_connect')
def spotify_connect():
    url_args = "&".join([f"{key}={urllib.parse.quote(val)}" for key, val in spotify_auth_query_parameters.items()])
    auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
    return redirect(auth_url)

@app.route('/callback/q')
def callback():
    auth_token = request.args['code']
    code_payload = {
        # 'grant_type': 'client_credentials',
        'grant_type': 'authorization_code',
        'code': str(auth_token),
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET
    }

    post_request = urllib.request.Request(
        SPOTIFY_TOKEN_URL,
        data = urllib.parse.urlencode(code_payload).encode()
    )

    post_request = urllib.request.urlopen(post_request)
    post_request = post_request.read()

    response_data = json.loads(post_request)
    access_token = response_data['access_token']
    refresh_token = response_data['refresh_token']
    token_type = response_data['token_type']
    expires_in = response_data['expires_in']

    session['access_token'] = access_token
    session['refresh_token']  = refresh_token
    session['expires_in'] = expires_in
    print(time.time())
    print(datetime.now())

    # req = urllib.request.Request(
    #     "https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V",
    #     headers=authorization_header,
    # )
    # req = urllib.request.urlopen(req)
    # res = req.read()
    # data = json.loads(res)

    # user_profile_api_endpoint = f"{SPOTIFY_API_URL}/me"
    # profile_response = urllib.request.Request(user_profile_api_endpoint, headers=authorization_header)
    # profile_response = urllib.request.urlopen(profile_response)
    # profile_response = profile_response.read()
    # profile_data = json.loads(profile_response)

    # Get user playlist data
    # playlist_api_endpoint = f"{profile_data['href']}/playlists"
    # playlists_response = urllib.request.Request(url=playlist_api_endpoint, headers=authorization_header)
    # playlists_response = urllib.request.urlopen(playlists_response)
    # playlists_response = playlists_response.read()
    # playlist_data = json.loads(playlists_response)

    # Combine profile and playlist data to display
    # display_arr = [profile_data] + playlist_data["items"]
    return redirect(url_for('root'))

if __name__ == '__main__':
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
