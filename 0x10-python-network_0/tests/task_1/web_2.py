#!/usr/bin/python3
"""Web Server"""
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """Root"""
    return redirect(url_for('redirect_1'), code=301)

@app.route("/redirect_1", strict_slashes=False)
def redirect_1():
    """redirect_1"""
    return redirect(url_for('redirect_2'), code=303)

@app.route("/redirect_2", strict_slashes=False)
def redirect_2():
    """redirect_2"""
    return redirect(url_for('redirect_3'), code=301)

@app.route("/redirect_3", strict_slashes=False)
def redirect_3():
    """redirect_3"""
    return redirect(url_for('redirect_4'), code=307)

@app.route("/redirect_4", strict_slashes=False)
def redirect_4():
    """redirect_4"""
    return redirect(url_for('redirect_5'), code=305) 

@app.route("/redirect_5", strict_slashes=False)
def redirect_5():
    """redirect_5"""
    return "With 5 redirections"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

