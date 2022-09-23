#!/usr/bin/python3
"""Web Server"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'], strict_slashes=False)
def index():
    """Root"""
    post_subject = request.form.get("subject")
    if post_subject is None:
        return "subject parameter missing"
    elif post_subject == "I will always be here for PLD":
        return "OK"
    return "wrong value of subject"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
