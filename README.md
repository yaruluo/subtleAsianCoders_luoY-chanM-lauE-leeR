# RYthEM by subtleAsianCoders

## Roster

- **Yaru Luo** (Project Manager):
  - Oversees & plans incremental project development mile-marks
  - Hosts github repo
  - Helps with minor frontend/backend development
  - Updates design doc, maintains devlog
- **Matthew Chan**
  - Write Python scripts to handle requests to modify or retrieve data from databases and APIs using HTTP/necessary OAuth
  - Make SQLAlchemy models for the database tables
  - Creates the GuessTheSong game
- **Eric "Morty" Lau**
  - Creates HTML templates and pages according to sitemap
  - Jinja
  - Bootstrap and custom CSS styling
    - We are using Bootstrap because we are all more comfortable with it and believe it looks better than Foundation
- **ray. lee.**
  - Write Python scripts to handle requests to modify or retrieve data from databases and APIs using HTTP/necessary OAuth
  - Make SQLAlchemy models for the database tables
  - Creates the Higher-Lower game

## Description

Our website is all about music! We want to create two games: HigherLower, wherein you guess which song of two shown have more listens, and GuessTheSong, wherein you are shown the lyrics to a song and guess what song it is (multiple choice). We also allow user's to connect connect with their own Spotify account and use their own liked songs in the games.

[video demo here](youtube.com)

## APIs Used

- [Spotify](https://docs.google.com/document/d/1hnI9zCld87HNG-7Vf2Qgeeb4gc08kQzHdCtFPKH0jd4/edit): Retrieves a user’s playlists, songs, and recommendations
- [Musixmatch](https://docs.google.com/document/d/1iOdEsoYiQ6hxNwFtRxu3Eh1aGIGiIwvMeSQFtFF-dOw/edit): Retrieves a song’s lyrics.

## Instructions

### Assuming python3 and pip are already installed

### Virtual Environment

- To prevent conflicts with globally installed packages, it is recommended to run everything below in a virtual environment.

Set up a virtual environment by running the following in your terminal:

```shell
python -m venv hero
# replace hero with anything you want
# If the above does not work, run with python3 (this may be the case if a version of python2 is also installed)
```

To enter your virtual environment, run the following:

```shell
. hero/bin/activate
```

To exit your virtual environment, run the following:

```shell
deactivate
```

### Dependencies

Run the following line in your virtual environment

```shell
pip install -r doc/requirements.txt
```

### Launch codes

#### Spotify

- Head over to [My Dashboard | Spotify for Developers](https://developer.spotify.com/dashboard/login)
- Log in with your Spotify account
- Click the button labeled "CREATE A CLIENT ID"
- Fill out the form with information about your application
- Your Client ID and Client Secret are shown on the dashboard for your app
- Click Edit Settings and add the following to Redirect URI: <http://127.0.0.1:5000/callback/q>
- Open `app/api.json` and paste your Client ID and Client Secret.

```json
    "SPOTIFY_CLIENT_ID": "",
    "SPOTIFY_CLIENT_SECRET": ""
```

#### Musixmatch

- Create a Musixmatch account [here](https://developer.musixmatch.com/signup)
- Go to your account screen and click the dashboard tab, and then click the applications tab.
- You should be able to see an API key listed next to your application in a table.
- Open `app/api.json` and paste your API key.

```json
    "MUSIXMATCH_API_KEY": ""
```

### Cloning

Run the following line in your terminal

```shell
git clone https://github.com/yaruluo/subtleAsianCoders_luoY-chanM-lauE-leeR.git
```

### Running

Run the following line in your virtual environment

```shell
python app/app.py
```

Open a browser and head to <http://127.0.0.1:5000/>
