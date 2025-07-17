from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

quotes = [
    {"quote": "Success is not final; failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Hard work beats talent when talent doesn’t work hard.", "author": "Tim Notke"}
]

# JSON API
@app.route("/quotes")
def get_all_quotes():
    return jsonify(quotes)

# HTML Page
@app.route("/")
def show_quotes_html():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Motivational Quotes</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
            .quote-box { background: white; padding: 15px; margin: 10px 0; border-left: 5px solid #2196F3; }
            .quote { font-size: 1.2em; }
            .author { font-style: italic; color: #555; margin-top: 5px; }
        </style>
    </head>
    <body>
        <h1>Motivational Quotes</h1>
        {% for q in quotes %}
            <div class="quote-box">
                <div class="quote">"{{ q.quote }}"</div>
                <div class="author">- {{ q.author }}</div>
            </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html_template, quotes=quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
