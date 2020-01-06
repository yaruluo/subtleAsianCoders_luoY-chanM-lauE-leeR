# _Duende_ by subtleAsianCoders

## Roster

- **Yaru Luo** (Project Manager):
  - Oversees project development
  - Help with frontend/backend development
  - Updates devlog and design doc
- **Eric "Morty" Lau**
  - Creates HTML templates and pages according to sitemap 
  - Jinja
  - Bootstrap and custom CSS styling 
    - We are using Bootstrap because we are all more comfortable with it and believe it looks better than Foundation
- **ray. lee.**
  - Write Python scripts to handle requests to modify or retrieve data from databases and APIs using HTTP/necessary OAuth 
  - Integrate code from the last project for the login features
  - Make SQLAlchemy models for the database tables
- **Matthew Chan**
  - Write Python scripts to handle requests to modify or retrieve data from databases and APIs using SQLite
  - Assist with retrieval from APIs using OAuth
  - SQLite/alchemy operations
    - Create, read, update, delete (CRUD) through SQLAlchemy to SQLite

## Description

## APIs Used

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

### Running

Run the following line in your virtual environment

```shell
python app.py
```

Open a browser and head to <http://127.0.0.1:5000/>
