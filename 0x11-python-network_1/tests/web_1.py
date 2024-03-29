#!/usr/bin/python3
"""Web Server"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'], strict_slashes=False)
def index():
    """Root"""
    email = request.form.get("email")
    if email is None:
        return "subject parameter missing"
    elif email == "test@mail.com":
        return "OK"
    return "wrong value of email"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
