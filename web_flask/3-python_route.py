#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask
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


@app.route('/python/(<text>)', strict_slashes=False)
def new(text="is cool"):
    updated_text = text.replace('_', ' ')
    return "Python %s" % escape(updated_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
