#!/usr/bin/python3
"""Web Server"""
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['OPTIONS', 'HEAD', 'DELETE'], strict_slashes=False)
def index():
    """Root"""
    return "DELETE method accepted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
