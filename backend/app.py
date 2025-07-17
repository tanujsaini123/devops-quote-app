from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {"quote": "Success is not final; failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Hard work beats talent when talent doesn’t work hard.", "author": "Tim Notke"}
]

@app.route("/quote")
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
