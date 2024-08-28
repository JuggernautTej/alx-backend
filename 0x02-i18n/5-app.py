#!/usr/bin/env python3
"""A simple flask app for the localization task"""

from flask import Flask, g, render_template, request
from flask_babel import _, Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """A class to keep track of supported languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """ function that returns a user dictionary or None if
    the ID cannot be found or if login_as was not passed."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """A function that use get_user to find a user if any,
    and set it as a global on flask.g.user."""
    g.user = get_user()


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
