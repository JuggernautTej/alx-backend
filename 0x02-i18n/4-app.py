#!/usr/bin/env python3
"""A simple flask app for the localization task"""

from flask import Flask, render_template, request
from flask_babel import _, Babel


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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Determines the best match for supported languages"""
    # Check if the locale parameter is in the URL request
    locale = request.args.get('locale')
    # return locale if it is present and one of the supported languages
    if locale in app.config['LANGUAGES']:
        return locale
    # Returns the best match from the Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
