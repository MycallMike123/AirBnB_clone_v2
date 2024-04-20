#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
It uses storage for fetching data from the storage
engine (FileStorage or DBStorage).
After each request, it removes the current SQLAlchemy Session.
Routes:
    /cities_by_states: display a HTML page with the list of all State
    objects present in DBStorage sorted by name (A->Z),
    along with the list of City objects linked to each
    State sorted by name (A->Z).
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session after each request"""

    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with the list of all State objects and their
    associated cities
    """

    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
