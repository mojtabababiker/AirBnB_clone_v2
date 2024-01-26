#!/usr/bin/python3
"""
flask application routes
"""
from models import storage
from models import *
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_page():
    """
    States route's page
    """
    states = storage.all(state.State).values()
    # print(list(states.values())[0].cities[0])
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def city_by_id_page(id):
    """
    States route's page
    """
    states = storage.all(state.State).values()

    return render_template('9-states.html', states=states, id=id)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
