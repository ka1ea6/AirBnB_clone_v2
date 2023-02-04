#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    '''Method to render an HTML page'''

    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run("0.0.0.0")