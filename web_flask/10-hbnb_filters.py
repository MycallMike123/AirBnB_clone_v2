#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
It uses storage for fetching data from the storage engine
(FileStorage or DBStorage).
After each request, it removes the current SQLAlchemy Session.
Routes:
    /hbnb_filters: display a HTML page like 6-index.html, which
    was done during the project 0x01. AirBnB clone - Web static
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a HTML page similar to 6-index.html with data from DBStorage"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
