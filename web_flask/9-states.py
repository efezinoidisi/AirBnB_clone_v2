#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from werkzeug.utils import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    data = storage.all(State)
    keys = data.keys()
    check = "State.{}".format(id)
    states = data.values()
    states = sorted(states, key=lambda l: l.name)
    value = False
    if check in keys:
        states = data.get(check)
        value = True
    return render_template('9-states.html', states=states, id=id, value=value)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
