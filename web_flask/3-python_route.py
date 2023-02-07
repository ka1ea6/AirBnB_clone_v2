#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
