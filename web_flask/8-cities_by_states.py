#!/usr/bin/python3
"""
<<<<<<< HEAD
A script that starts a Flask web application:
"""

from flask import Flask
from models import storage
from flask import render_template

=======
A script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
<<<<<<< HEAD
def cities_by_states_route():
    """
    Cities by states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists all states sort by name A->Z
    """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
