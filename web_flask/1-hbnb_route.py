#!/usr/bin/python3
<<<<<<< HEAD
"""
A script that starts a Flask web application:
"""

from flask import Flask

=======
""" A script that start a Flask web application with 2 commands """

from flask import Flask


>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
