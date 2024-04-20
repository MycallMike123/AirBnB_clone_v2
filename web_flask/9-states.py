#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
It uses storage for fetching data from the storage engine
(FileStorage or DBStorage)
After each request, it removes the current SQLAlchemy Session.
Routes:
    /states: display a HTML page with the list of all State objects
    present in DBStorage sorted by name (A->Z)
    /states/<id>: display a HTML page with the list of City objects
    linked to the State with the given id
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Display a HTML page with the list of all State
    objects present in DBStorage"""

    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display a HTML page with the list of City objects linked to the
    State with the given id
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
