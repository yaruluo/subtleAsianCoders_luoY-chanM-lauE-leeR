'''
subtleAsianCoders - Yaru Luo, Matthew Chan, Eric "Morty" Lau, ray. lee.
SoftDev1 pd1
P02 -- The End
RYthEM
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
import random
import json
import datetime
import random

api_file = os.path.dirname(os.path.abspath(__file__)) + '/api.json'

# TODO: remove api keys from the file after development is done

with open( api_file, 'r') as read_file:
    keys = json.load( read_file) # retrieve keys from json

SPOTIFY_CLIENT_ID = keys[ 'SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = keys[ 'SPOTIFY_CLIENT_SECRET']
MUSIXMATCH_API_KEY = keys[ 'MUSIXMATCH_API_KEY']

# SQLAlchemy DB Models
db = models.db
Song = models.Song
Album = models.Album
UserSongs = models.UserSongs

app = Flask(__name__)
app.config.from_object( Config)

# creates secret key for sessions
app.secret_key = os.urandom( 32)

# MUSIXMATCH_API_KEY = open('secret', 'r').read()

# renders spotify api url data vis a vis ur own spotify account
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
SPOTIFY_API_VERSION = 'v1'
SPOTIFY_API_URL = f"{SPOTIFY_API_BASE_URL}/{SPOTIFY_API_VERSION}"

CLIENT_SIDE_URL = 'http://127.0.0.1'
PORT = 5000
SPOTIFY_REDIRECT_URI = f"{CLIENT_SIDE_URL}:{PORT}/callback/q"
SPOTIFY_SCOPE = 'user-library-read user-library-modify user-top-read'

spotify_auth_query_parameters = {
    'client_id': SPOTIFY_CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': SPOTIFY_REDIRECT_URI,
    'scope': SPOTIFY_SCOPE,
}

#========================================================================================
# HELPER FUNCTIONS

#----------------------------------------------------------------------------------
# API FUNCTIONS
def spotify_api_query(url, method):
    authorization_header = {
        'Authorization': f"Bearer {session['access_token']}"
    }
    req = urllib.request.Request(
        url,
        headers=authorization_header,
        method=method,
    )
    req = urllib.request.urlopen(req)

    if method == 'GET':
        res = req.read()
        data = json.loads(res)
        return data
    return None


'''
Accesses the Musixmatch API and returns the lyrics and genre of a given song title and/or artist and/or album
'''
def musixmatch_api_query(title='', artist='', album=''):
    # Search for the song
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
    url = urllib.request.urlopen(search_request)
    search_json = json.loads(url.read())
    # print(search_request)

    body = search_json['message']['body']
    if (body != ''):
        track_id = search_json['message']['body']['track']['track_id']
        
        music_genre_list = search_json['message']['body']['track']['primary_genres']['music_genre_list']
        if (len(music_genre_list) == 0):
            genre = "GENRE NOT AVAILABLE"
        else:
            genre = music_genre_list[0]['music_genre']['music_genre_name']

        has_lyrics = search_json['message']['body']['track']['has_lyrics']
        if (has_lyrics == 1):
            # Get the lyrics for the found song
            lyrics_request = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?'
            lyrics_request += 'track_id=' + str(track_id)
            lyrics_request += '&apikey=' + MUSIXMATCH_API_KEY
            # print(lyrics_request)
            url = urllib.request.urlopen(lyrics_request)
            lyrics_json = json.loads(url.read())
            print(lyrics_request)
            lyrics = lyrics_json['message']['body']['lyrics']['lyrics_body']
        else:
            lyrics = 'LYRICS NOT AVAILABLE'
    else:
        genre = "GENRE NOT AVAILABLE"
        lyrics = 'LYRICS NOT AVAILABLE'

    # Package the API data
    data = dict()
    data['lyrics'] = lyrics
    data['genre'] = genre
    return data

#----------------------------------------------------------------------------------

def get_user_name():
    data = spotify_api_query("https://api.spotify.com/v1/me/", 'GET')
    session['display_name'] = data['display_name']
    session['spotify_user_id'] = data['id']


def get_user_hearted():
    data = spotify_api_query("https://api.spotify.com/v1/me/tracks?limit=50", 'GET')['items']
    sids = cache_songs(data)
    for sid in sids:
        user_song_link(session['spotify_user_id'], sid)


def cache_songs(songs):
    sids = list()
    for song in songs:
        artist = song['track']['album']['artists'][0]['name']
        title = song['track']['name']
        genre = ''
        lyrics = ''
        popularity = -1
        spotifyid = ''
        iframe = ''
        album = ''
        coverartlink = ''

        cachedSong = Song.query.filter_by(title = title, artist=artist).first()
        if (cachedSong != None):
            sids.append(cachedSong.sid)
        else:
            coverartlink = song['track']['album']['images'][0]['url']
            popularity = song['track']['popularity']

            spotifyid = song['track']['id']
            track_link = song['track']['external_urls']['spotify']
            iframe = f"{track_link[:25]}embed/{track_link[25:]}"

            albumType = song['track']['album']['album_type']
            # TODO: problems with non-standard characters in album names like "÷ (Deluxe)"
            if (albumType == "single"):
                album = f"SINGLE|{title}:{artist}"
                musixmatch_data = musixmatch_api_query(title=title, artist=artist)
            else:
                album = song['track']['album']['name']
                musixmatch_data = musixmatch_api_query(title=title, artist=artist, album=album)
            
            if ((musixmatch_data['lyrics'] != "LYRICS NOT AVAILABLE") and (musixmatch_data['genre'] != "GENRE NOT AVAILABLE")):
                lyrics = musixmatch_data['lyrics']
                if (lyrics != "LYRICS NOT AVAILABLE"):
                    lyrics = lyrics[:((lyrics.find('*'))-1)]
                genre = musixmatch_data['genre']
                
                # add songs to database
                aid = -1
                cachedAlbum = Album.query.filter_by(title = album).first()
                if (cachedAlbum != None):
                    aid = cachedAlbum.aid
                else:
                    albumObject = Album(title=album, coverartlink=coverartlink)
                    db.session.add(albumObject)
                    db.session.commit()

                    lastAddedAlbum = db.session.query(Album).order_by(Album.aid.desc()).first()
                    aid=lastAddedAlbum.aid
                
                songObject = Song(
                    aid=aid,
                    artist=artist,
                    title=title,
                    genre=genre,
                    lyrics=lyrics,
                    popularity=popularity,
                    spotifyid=spotifyid,
                    iframe=iframe
                )
                db.session.add(songObject)
                db.session.commit()

                lastAddedSong = db.session.query(Song).order_by(Song.sid.desc()).first()
                sids.append(lastAddedSong.sid)

    return sids


def user_song_link(spotify_id, song_id):
    cachedLink = UserSongs.query.filter_by(spotifyid=spotify_id, sid=song_id).first()
    if (cachedLink != None):
        return None
    link = UserSongs(spotifyid = spotify_id, sid=song_id)
    db.session.add(link)
    db.session.commit()


def get_user_songs(numSongs):
    links = UserSongs.query.filter_by(spotifyid=session['spotify_user_id']).all()
    random.shuffle(links)
    links = links[0:numSongs]

    songObjects = list()
    for link in links:
        songObject = Song.query.filter_by(sid=link.sid).first()
        songObjects.append(songObject)
    return songObjects


def get_guest_songs(numSongs):
    links = UserSongs.query.filter_by(spotifyid='guest').all()
    random.shuffle(links)
    links = links[0:numSongs]

    songObjects = list()
    for link in links:
        songObject = Song.query.filter_by(sid=link.sid).first()
        songObjects.append(songObject)
    return songObjects


def package_song(songObject):
    songDict = dict()
    songDict['artist'] = songObject.artist
    songDict['title'] = songObject.title
    songDict['popularity'] = songObject.popularity
    songDict['spotify_id'] = songObject.spotifyid
    songDict['iframe'] = songObject.iframe
    return songDict

#========================================================================================


# checks if logged in to ur Spotify acc
def protected( f):
    @functools.wraps( f)
    def wrapper( *args, **kwargs):
        if 'access_token' in session:
            # if logged in, continue with expected function
            return f( *args, **kwargs)
        else:
            flash( 'You are not connected to your Spotify account', 'error')
            return redirect( url_for( 'home'))
    return wrapper


@app.route( '/')
def home():
    return render_template(
        'home.html',
    )

@app.route( '/spotify_connect')
def spotify_connect():
    url_args = "&".join( [ f"{key}={urllib.parse.quote(val)}" for key,
                         val in spotify_auth_query_parameters.items()])
    auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
    return redirect( auth_url)

@app.route('/callback/q')
def callback():
    auth_token = request.args['code']
    code_payload = {
        'grant_type': 'authorization_code',
        'code': str(auth_token),
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET
    }

    post_request = urllib.request.Request(
        SPOTIFY_TOKEN_URL,
        data=urllib.parse.urlencode(code_payload).encode()
    )

    post_request = urllib.request.urlopen(post_request)
    post_request = post_request.read()

    response_data = json.loads(post_request)
    access_token = response_data['access_token']
    refresh_token = response_data['refresh_token']
    token_type = response_data['token_type']
    expires_in = response_data['expires_in']

    session['access_token'] = access_token

    get_user_name()
    get_user_hearted()

    return redirect(url_for('home'))


@app.route('/guess_the_song')
def guess_the_song():
    if 'access_token' in session:
        isLoggedIn = "True"
    else:
        isLoggedIn = "False"
    return render_template('guess_the_song.html', isLoggedIn=isLoggedIn)


@app.route('/guess_the_song/<choice>')
def play(choice):
    if (choice == 'random'):
        songObjects = get_guest_songs(10)
    if (choice == 'my_songs'):
        songObjects = get_user_songs(10)

    songsDict = dict()
    for i in range(10):
        availableChoices = list(songObjects)
        availableChoices.pop(i)
        choices = random.sample(availableChoices, k=3)
        choices.append(songObjects[i])
        random.shuffle(choices)
        songsDict[songObjects[i]] = choices
    return render_template('guess_the_song_game.html', songs=songsDict)
    

@app.route('/higher_lower/<choice>')
def higher_lower(choice):
    if choice == 'screen':
        return render_template(
            'higherlowerscreen.html',
            )
    elif choice == 'random':
        return render_template(
            'higherlowergame.html',
            songs=session['songs'],
            choice = choice
            )
    if choice == 'favorite':
        if 'access_token' in session:
            return render_template(
                'higherlowergame.html',
                songs=session['songs'],
                choice = choice
            )
        else:
            flash( 'You are not connected to your Spotify account', 'error')
            return redirect(url_for('home'))

@protected # openable if connected
@app.route("/save_song/<song_id>")
def save_song( song_id):
    spotify_api_query( f"https://api.spotify.com/v1/me/tracks?ids={song_id}", 'PUT')
    return redirect( url_for( 'hearted_songs'))

@protected
@app.route("/hearted_songs")
def hearted_songs():

    data = spotify_api_query("https://api.spotify.com/v1/me/tracks?limit=10", 'GET')

    return render_template(
        "hearted_songs.html",
        data = data['items'],
    )

@protected
@app.route("/cache")
def cache():
    data = spotify_api_query("http://api.spotify.com/v1/playlists/37i9dQZF1DXbYM3nMM0oPk", 'GET')['tracks']['items']
    sids = cache_songs(data)
    for sid in sids:
        user_song_link('guest', sid)

    return render_template(
        "test.html",
        data = data
    )

@app.route('/logout')
def logout():
    session['access_token'] = None
    session['display_name'] = None
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(
        debug=True,
        threaded=True
        )
