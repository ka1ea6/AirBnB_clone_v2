#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    '''Displays Hello, HBNB for requests to /'''
    return 'Hello, HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
