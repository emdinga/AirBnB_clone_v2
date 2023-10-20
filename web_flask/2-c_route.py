#!/usr/bin/python3
""" Web application to start flask"""
from falsk import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')

if __name__ = "__main__":
	""" Main Function """
	app.run(host='0.0.0.0', port=5000)
