#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask, escape

app = Flask(__name__)


@app.route("/")
def index():
    '''Displays Hello, HBNB for requests to /'''
    return 'Hello, HBNB!'


@app.route("/hbnb")
def hbnb():
    '''Displays HBNB for requests to /hbnb'''
    return 'HBNB'


@app.route("/c/<text>")
def c_is_fun(text):
    '''Displays "c" followed by the value of text'''
    return 'C %s' % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
