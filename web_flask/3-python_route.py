#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
               (replace underscore _ symbols with a space)
    /python/<text>: display “Python ”, followed by the value of the text
                    variable (replace underscore _ symbols with a space)
The default value of text is “is cool”
The option strict_slashes=False is used in route definitions.
"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display "Hello HBNB!" on the index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "HBNB" on the /hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display "C ", followed by the value of the text variable"""
    return "C " + unquote(text).replace("_", " ")


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display “Python ”, followed by the value of the text variable"""
    return "Python " + unquote(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
