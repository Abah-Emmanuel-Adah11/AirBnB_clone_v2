#!/usr/bin/python3
"""
<<<<<<< HEAD
A script that starts a Flask web application:
=======
starting Flask web application
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def hello_hbnb():
    """ To return Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
