#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from werkzeug.utils import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    data = storage.all(State).values()
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def close_db(error):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
