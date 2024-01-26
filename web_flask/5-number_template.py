#!/usr/bin/python3
"""
module for application routes
"""
from flask import Flask
from flask import render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool_page(text='is cool'):
    """
    Just a random route to explain variables
    on the URL
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_page(n):
    """
    Just a random route to explain variables
    on the URL
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template_page(n):
    """
    Just a random route to explain variables
    on the URL, and rendering templates
    """
    return render_template('5-number.html', number=n)


app.run('0.0.0.0', port=5000)
