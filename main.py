from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [f"Film {i}" for i in range(1, 11)]  # Generowanie listy 10 filmów
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
