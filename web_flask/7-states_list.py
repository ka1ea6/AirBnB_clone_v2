#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states_list")
def states_list():
    '''Method to render an HTML page'''
    from models import storage

    return f"{storage.all()}"

if __name__ == "__main__":
    app.run("0.0.0.0")