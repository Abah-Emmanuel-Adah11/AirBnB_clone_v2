#!/usr/bin/python3
"""
<<<<<<< HEAD
A script that starts a Flask web application:
"""

from flask import Flask
from models import storage
from flask import render_template

=======
starting a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
<<<<<<< HEAD
def states_list_route():
    """
    List states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists all states sort by name A->Z
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id_route(id):
    """
    Get a state by id
    Returns:
        html: template that lists cities of state sort by name A->Z
    """
    state = None
    for s in storage.all("State").values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> f44ee2d87fc5aa53b6123fb4f099817475fd3c05
