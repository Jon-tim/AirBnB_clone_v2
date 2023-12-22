#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -   Web application must be listening on 0.0.0.0, port 5000
    -   Routes:
                /: display “Hello HBNB!”
                /hbnb: display “HBNB”
                /c/<text>: display “C ” followed by the value of
                    the text variable
                    (replace underscore _ symbols with a space )
    -   Uses the option strict_slashes=False in the route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """function that returns Hello HBNB"""
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function that defines another route"""
    return "<p>HBNB</p>"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """function that uses a variable to define route"""
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
