#!/usr/bin/env python3
""" doc doc doc """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """doc doc doc"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselctor
def get_locale() -> str:
    """ doc doc doc """
    if request.args.get("locale") in app.config["LANGUAGE"]:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """doc doc doc"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
