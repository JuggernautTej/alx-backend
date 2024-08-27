#!/usr/bin/env python3
"""A simple flask app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """A class to keep track of supported languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello_world():
    """This outputs hello world as a header"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
