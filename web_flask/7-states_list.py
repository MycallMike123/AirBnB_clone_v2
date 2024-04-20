#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
It uses storage for fetching data from the storage engine
After each request, it removes the current SQLAlchemy Session
Routes:
    /states_list: display a HTML page with the list of all State
    objects present in DBStorage sorted by name (A->Z)
"""

from flask import Flask, render_template
from models import storage
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of all State objects"""
    sorted_states = sorted(list(storage.all("State").
                                values()), key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
