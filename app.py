'''
subtleAsianCoders - Yaru Luo, Eric "Morty" Lau, Raymond Lee, Matthew Chan
SoftDev1 pd1
P02 -- The End
'''

from flask import Flask, request, redirect, session, render_template, url_for, flash
import sqlite3
import urllib.request
import urllib.parse
import functools
import os
import json
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def root():
    return render_template(
        'index.html'
    )

if __name__ == '__main__':
    app.debug = True
    app.run()