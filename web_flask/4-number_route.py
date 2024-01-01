#!/usr/bin/python3
<<<<<<< HEAD
"""
A script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    display “C ” followed by the value of the text variable
        (replace underscore '_' symbols with a space ' ')
    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    display “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    display “n is a number” only if n is an integer
    Returns:
        int: the value of n
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
""" it add fourth view function that displays var only if is integer """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replacing more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
