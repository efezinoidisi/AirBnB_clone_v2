#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This route returns hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    updated_text = text.replace('_', ' ')
    return "C %s" % escape(updated_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def new(text="is cool"):
    updated_text = text.replace('_', ' ')
    return "Python %s" % escape(updated_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    if n % 2 == 0:
        value = "even"
    else:
        value = "odd"
    return render_template('6-number_odd_or_even.html', n=n, value=value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
