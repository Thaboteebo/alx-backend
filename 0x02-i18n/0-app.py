#!/usr/bin/env python3
"""doc doc doc"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """doc doc doc"""
    return render_template("0-index.html")


if __name__ == "__name__":
    app.run(host="0.0.0.0", port="5000")
