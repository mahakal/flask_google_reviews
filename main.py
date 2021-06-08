from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
