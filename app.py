from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
db = SQLAlchemy(app)

DATABASE = "games.db"

# Game Model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(100), nullable=False)
    platforms = db.Column(db.String(200), nullable=False)
    developer = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    metacritic_score = db.Column(db.Integer, nullable=False)

# Home/Search Page
@app.route('/')
def search():
    games = Game.query.all()
    return render_template('search.html', games=games)

# Search API for AJAX filtering
@app.route('/search', methods=['POST'])
def search_games():
    query = request.json.get("query", "").lower()
    min_score = int(request.json.get("min_score", 0))
    max_score = int(request.json.get("max_score", 100))

    games = Game.query.all()

    filtered_games = [
        {"id": game.id, "title": game.title, "score": game.metacritic_score} 
        for game in games 
        if (query in game.title.lower() or query in game.genre.lower() or 
            query in game.platforms.lower() or query in game.developer.lower()) 
        and (min_score <= game.metacritic_score <= max_score)
    ]
    
    return jsonify(filtered_games)

# Game Details Page
@app.route('/game/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to get games from the database
def get_games():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    conn.close()
    return games

@app.route('/')
def home():
    games = get_games()
    return render_template('search.html', games=games)

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE id=?", (game_id,))
    game = cursor.fetchone()
    conn.close()
    return render_template('game.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)

