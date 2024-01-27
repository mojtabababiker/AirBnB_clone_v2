#!/usr/bin/python3
"""
HBNB CLone Filter routes
"""
from models import storage
from models import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    HBNB filters route page
    """
    states = storage.all(state.State)
    amenities = storage.all(amenity.Amenity)

    return render_template('10-hbnb_filters.html')


@app.teardown_appcontext
def handle_teardown(err=None):
    """
    Handle application teardown and close the connection
    """
    try:
        storage.close()
    except Exception as er:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
