#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
It uses storage for fetching data from the storage engine
(FileStorage or DBStorage)
After each request, it removes the current SQLAlchemy Session.
Routes:
    /hbnb: display a HTML page similar to 8-index.html from
    the AirBnB clone project
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
