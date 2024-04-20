#!/usr/bin/python3

"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
               (replace underscore _ symbols with a space)
    /python/(<text>): display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space)
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
                           H1 tag: “Number: n” inside the tag BODY
The default value of text is “is cool”
The option strict_slashes=False is used in route definitions.
"""

from flask import Flask, render_template

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
    """Display “C ”, followed by the value of the text variable"""
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display “Python ”, followed by the value of the text variable"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page with 'Number: n' in H1 tag"""
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
