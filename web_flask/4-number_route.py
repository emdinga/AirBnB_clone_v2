#!/usr/bin/python3
""" start a Flask web application"""

from flask import Flask
app = Flask(__name__)



@app.route('/', strict_slashes=False)
def hello_hbnb():
""" print a massage"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ dsiplay hbnb"""
	return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints a Message when c """
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Prints a Message when python """
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """ Prints a Message number only if n is an int"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
