#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Displays Hello, HBNB for requests to /'''
    return 'Hello, HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays HBNB for requests to /hbnb'''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
