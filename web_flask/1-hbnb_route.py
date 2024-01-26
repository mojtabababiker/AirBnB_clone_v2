#!/usr/bin/python3
"""
module for application routes
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home page route which render the
    'Hello HBNB!' message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def home():
    """
    hbnb page route which render the
    'HBNB!' message
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
