#!/usr/bin/python3
"""
HBnb-Clone full route module
"""
from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_hose():
    """
    Landing page of the HBnB-clone web application
    """
    states = storage.all(state.State).values()
    amenities = storage.all(amenity.Amenity).values()
    places = storage.all(place.Place).values()
    users = storage.all(user.User).values()

    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def teardown_request(err=None):
    """
    handle the teardown of each request by
    calling storage.close() to force session close
    """
    try:
        storage.close()
    except Exception as er:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
