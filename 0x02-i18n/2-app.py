#!/usr/bin/env python3
"""simple flask app"""
from flask import Flask
from flask_babel import Babel
from flask import render_template
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configures available languages"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gets the best match from supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    """Renders the hello world template"""

    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
