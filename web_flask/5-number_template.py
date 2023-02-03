#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask, escape, render_template

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


@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    '''Displays "python" folllowed by the value of text'''
    return 'Python %s' % escape(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    '''Displays "n" is a number if n is an integer'''
    if isinstance(n, int):
        return '%d is a number' % n
    else:
        return ''


@app.route("/number_template/<int:n>")
def number_template(n=None):
    '''Display an html page only if n is an integer'''
    if isinstance(n, int):
        print(n)
        return render_template("5-number.html", n=n)
    else:
        return ''


if __name__ == "__main__":
    app.run(host="0.0.0.0")
