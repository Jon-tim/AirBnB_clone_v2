#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -   Web application must be listening on 0.0.0.0, port 5000
    -   Routes:
                /: display “Hello HBNB!”
    -   Uses the option strict_slashes=False in the route definition
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """function that returns Hello HBNB"""
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
