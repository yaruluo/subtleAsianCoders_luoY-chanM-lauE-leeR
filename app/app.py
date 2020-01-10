'''
subtleAsianCoders - Yaru Luo, Matthew Chan, Eric "Morty" Lau, ray. lee.
SoftDev1 pd1
P02 -- The End
Duende
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

MUSIXMATCH_API_KEY = open('secret', 'r').read()

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
def home():
    return render_template(
        'home.html',
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

    return redirect(url_for('home'))


@app.route('/guess_the_song')
def guess_the_song():
    return render_template('guess_the_song.html')


'''
Accesses the Musixmatch API and returns the lyrics of a given song title and/or artist and/or album
'''
def musixmatch_get(title='', artist='', album=''):
    #===SEARCHING=FOR=SONG==========================
    search_request = 'https://api.musixmatch.com/ws/1.1/matcher.track.get?'
    arguments = list()
    if (len(title) != 0):
        title = 'q_track=' + urllib.parse.quote(title)
        arguments.append(title)
    if (len(artist) != 0):
        artist = 'q_artist=' + urllib.parse.quote(artist)
        arguments.append(artist)
    if (len(album) != 0):
        album = 'q_album=' + urllib.parse.quote(album)
        arguments.append(album)
    search_request += '&'.join(arguments)
    search_request += '&apikey=' + MUSIXMATCH_API_KEY
    # print(search_request)
    url = urllib.request.urlopen(search_request)
    search_json = json.loads(url.read())

    track_id = search_json['message']['body']['track']['track_id']
    genre = search_json['message']['body']['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']

    has_lyrics = search_json['message']['body']['track']['has_lyrics']
    if (has_lyrics == 1):
        #===GETTING=LYRICS==============================
        lyrics_request = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?'
        lyrics_request += 'track_id=' + str(track_id)
        lyrics_request += '&apikey=' + MUSIXMATCH_API_KEY
        # print(lyrics_request)
        url = urllib.request.urlopen(lyrics_request)
        lyrics_json = json.loads(url.read())

        lyrics = lyrics_json['message']['body']['lyrics']['lyrics_body']
    else:
        lyrics = 'LYRICS NOT AVAILABLE'
    
    #===FORMATTING=MUSIXMATCH=DATA==================
    data = dict()
    data['lyrics'] = lyrics
    data['genre'] = genre
    return data

@app.route('/guess_the_song/play')
def play():
    # choose 10 random songs from Spotify
    # TODO: change temporary song sample to randomization============================
    f = open('dummysongs.json', 'r')
    songs = json.loads(f.read())
    # ===============================================================================

    # access Musixmatch lyrics for each song
    for song in songs['items']:
        title = song['track']['name']

        # TODO: currently assumes only one artist, potentially change to store all later on
        artist = song['track']['album']['artists'][0]['name']

        # TODO: potentially account for multiple album cover art variants
        coverArtLink = song['track']['album']['images'][0]['url']

        popularity = song['track']['popularity']

        album_type = song['track']['album']['album_type']
        # TODO: problems with non-standard characters in album names like "÷ (Deluxe)"
        if (album_type == "single"):
            album = "single"
            musixmatch_data = musixmatch_get(title=title, artist=artist)
        else:
            album = song['track']['album']['name']
            musixmatch_data = musixmatch_get(title=title, artist=artist, album=album)
        lyrics = musixmatch_data['lyrics']
        genre = musixmatch_data['genre']
        print(f'{title}|{artist}|{coverArtLink}|{popularity}|{album}|{genre}|{lyrics}')
    
    # TODO: add songs to database

    return render_template('guess_the_song_game.html')


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)