#!/usr/bin/python3
"""
module for application routes
"""
from flask import Flask
from web_flask import *


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


app.run('0.0.0.0', port=5000)
