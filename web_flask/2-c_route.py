#!/usr/bin/python3
"""
module for application routes
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """
    home page route which render the
    'Hello HBNB!' message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    hbnb page route which render the
    'HBNB!' message
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun_page(text):
    """
    Just a random route to explain variables
    on the URL
    """
    return f"C {text.replace('_', ' ')}"


app.run('0.0.0.0', port=5000)
