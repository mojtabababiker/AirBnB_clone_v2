#!/usr/bin/python3
"""
flask application routes
"""
from models import storage
from models import *
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_by_state_page():
    """
    States route's page
    """
    states = storage.all(state.State).values()
    # print(list(states.values())[0].cities[0])
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close(err=None):
    """
    handle the application tearDown, and call the close
    on the storage object
    """
    try:
        storage.close()

    except Exception as er:
        # TODO: log them in errors.log
        pass


app.run('0.0.0.0', port=5000, debug=True)
