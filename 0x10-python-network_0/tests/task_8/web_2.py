#!/usr/bin/python3
"""Web Server"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'], strict_slashes=False)
def index():
    """Root"""
    try:
        j = request.get_json(force=False, silent=True, cache=False)
        if j is not None:
            return "Valid"
    except Exception:
        pass
    return "NO"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
