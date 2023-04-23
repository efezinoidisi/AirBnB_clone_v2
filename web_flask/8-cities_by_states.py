#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from werkzeug.utils import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    data = storage.all(State).values()
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
