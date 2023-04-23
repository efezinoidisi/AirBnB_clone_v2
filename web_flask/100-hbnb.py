#!/usr/bin/python3
"""
This module contains a simple flask application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
#from models.user import User
from models.place import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
