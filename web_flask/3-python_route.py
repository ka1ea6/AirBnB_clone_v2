#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask, escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Displays Hello, HBNB for requests to /'''
    return 'Hello, HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays HBNB for requests to /hbnb'''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    '''Displays "c" followed by the value of text'''
    return 'C %s' % escape(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    '''Displays "python" folllowed by the value of text'''
    return 'Python %s' % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
