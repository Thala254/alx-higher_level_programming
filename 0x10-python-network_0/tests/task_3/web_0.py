#!/usr/bin/python3
"""Web Server"""
from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['OPTIONS', 'HEAD', 'GET'], strict_slashes=False)
def index():
    """Root"""
    res = Response("3 methods allowed")
    res.headers["Allow"] = "OPTIONS, HEAD, GET"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
