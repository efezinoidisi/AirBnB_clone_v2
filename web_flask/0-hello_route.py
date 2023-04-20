#!/usr/bin/python3
"""
This module contains a single route '/'
"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This route returns hello hbnb"""
    return 'Hello HBNB!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
