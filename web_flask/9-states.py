#!/usr/bin/python3
'''Starts a Flask web application.

It will start listening to requests comming
to 0.0.0.0 port 5000
'''

from models import storage
from flask import Flask, render_template
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states_list():
    '''Method to render an HTML page'''
    states = storage.all("State")

    return render_template("9-states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def state(state_id):
    '''Method to render an HTML page for a state'''
    states = storage.all("State")
    state = filter(lambda el: el.id == state_id, states)
    if state is None:
        return render_template("9-states.html")
    return render_template("9-states.html", state=state)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run("0.0.0.0")