from flask import Flask, render_template_string
import random

app = Flask(__name__)

quotes = [
    {"quote": "Success is not final; failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Hard work beats talent when talent doesn’t work hard.", "author": "Tim Notke"}
]

colors = ["#f8d7da", "#d1ecf1", "#d4edda", "#fff3cd", "#e2e3e5", "#f5c6cb", "#c3e6cb", "#ffeeba"]

@app.route("/")
def home():
    colored_quotes = [
        {**q, "color": random.choice(colors)}
        for q in quotes
    ]

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Colorful Motivational Quotes</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f0f2f5;
                padding: 30px;
                font-family: Arial, sans-serif;
            }
            .quote-card {
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            .quote-text {
                font-size: 1.3rem;
                font-weight: bold;
            }
            .quote-author {
                text-align: right;
                font-style: italic;
                margin-top: 10px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="mb-4 text-center text-primary">🌈 Motivational Quotes</h1>

            {% for q in quotes %}
            <div class="quote-card" style="background-color: {{ q.color }}">
                <div class="quote-text">“{{ q.quote }}”</div>
                <div class="quote-author">– {{ q.author }}</div>
            </div>
            {% endfor %}

            <div class="text-center">
                <a href="/" class="btn btn-primary mt-3">🔁 Refresh Colors</a>
            </div>
        </div>
    </body>
    </html>
    """

    return render_template_string(html, quotes=colored_quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
