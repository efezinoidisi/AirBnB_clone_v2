#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from werkzeug.utils import escape
from models import storage


app = Flask(__name__)
data = storage.all()


@app.route('/states_list', strict_slashes=False)
def state_list():
    return render_template('7-states_list.html')


@app.teardown_appcontext
def close_db(error):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
