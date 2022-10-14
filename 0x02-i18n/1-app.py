#!/usr/bin/env python3
"""simple flask app"""
from flask import Flask
from flask_babel import Babel
from flask import render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configures available languages"""
    
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)


@app.route("/")
def hello_world():
    """Renders the hello world template"""

    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
