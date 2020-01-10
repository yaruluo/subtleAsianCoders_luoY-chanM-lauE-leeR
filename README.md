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
  - Integrate code from the last project for the login features
  - Make SQLAlchemy models for the database tables
  - Creates the Higher-Lower game

## Description

Our website is all about music! We want to create two games: HigherLower, wherein you guess which song of two shown have more listens, and GuessTheSong, wherein you are shown the lyrics to a song and guess what song it is (multiple choice). We also want to use connect with the user's own Spotify account and use their own liked songs in the games.

## APIs Used

- [Spotify](https://docs.google.com/document/d/1NzepXhw6sM25KSLzbiNWgba3o53HcN3f8C2SMiajK5Q/edit): Retrieves a user’s playlists, songs, and recommendations
- [Genius](https://docs.google.com/document/d/1kJ05CPz_bWl5i77SlhBKSEpVl-J8EKPTACczuD9kZkE/edit): Retrieves a song’s lyrics.

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

### Cloning

```shell
git clone https://github.com/yaruluo/subtleAsianCoders_luoY-chanM-lauE-leeR.git
```

### Running

Run the following line in your virtual environment

```shell
python app/app.py
```

Open a browser and head to <http://127.0.0.1:5000/>
