from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)
DATABASE = 'Popular_Games.db'  # Your database file

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable column access by name
    return conn

# Base query joining all required tables.
GAME_SELECT = """
SELECT 
    games.game_id,
    games.title,
    games.genre,
    games.release_date,
    games.metacritic_score,
    games.description,
    developers.name AS developer,
    publishers.name AS publisher,
    age_ratings.rating AS age_rating,
    age_ratings.reason AS age_rating_reason,
    images.cover_image,
    images.image_url,
    images.image_url2,
    images.image_url3
FROM games
JOIN developers ON games.developer_id = developers.developer_id
JOIN publishers ON games.publisher_id = publishers.publisher_id
JOIN age_ratings ON games.age_rating_id = age_ratings.age_rating_id
JOIN images ON games.game_id = images.game_id
"""

@app.route('/')
def home():
    conn = get_db_connection()
    games = conn.execute(GAME_SELECT).fetchall()
    conn.close()
    return render_template("index.html", all_games=games)

# The search page now fetches up to 20 publishers and 20 developers.
@app.route('/search')
def search():
    conn = get_db_connection()
    publishers = conn.execute("SELECT name FROM publishers LIMIT 20").fetchall()
    developers = conn.execute("SELECT name FROM developers LIMIT 20").fetchall()
    conn.close()
    return render_template("search.html", publishers=publishers, developers=developers)

@app.route('/search_by_title', methods=["POST"])
def search_by_title():
    search_term = request.form.get("search_term", "").strip()
    query = GAME_SELECT + " WHERE (games.title LIKE ? COLLATE NOCASE OR developers.name LIKE ? COLLATE NOCASE OR publishers.name LIKE ? COLLATE NOCASE)"
    wildcard = f"%{search_term}%"
    params = [wildcard, wildcard, wildcard]
    conn = get_db_connection()
    results = conn.execute(query, tuple(params)).fetchall()
    conn.close()
    return render_template("search_results.html", results=results, search_type="Title/Developer/Publisher", search_value=search_term)

@app.route('/search_by_score', methods=["POST"])
def search_by_score():
    score_min = request.form.get("score_min", "").strip()
    score_max = request.form.get("score_max", "").strip()
    if not score_min:
        score_min = 0
    if not score_max:
        score_max = 100
    query = GAME_SELECT + " WHERE games.metacritic_score >= ? AND games.metacritic_score <= ?"
    params = [int(score_min), int(score_max)]
    conn = get_db_connection()
    results = conn.execute(query, tuple(params)).fetchall()
    conn.close()
    return render_template("search_results.html", results=results, search_type="Metacritic Score", search_value=f"{score_min} to {score_max}")

@app.route('/search_by_date', methods=["POST"])
def search_by_date():
    date_min = request.form.get("date_min", "").strip()
    date_max = request.form.get("date_max", "").strip()
    try:
        date_min_obj = datetime.strptime(date_min, "%Y-%m-%d")
        date_max_obj = datetime.strptime(date_max, "%Y-%m-%d")
    except ValueError:
        error = "Invalid date format. Please use YYYY-MM-DD."
        return render_template("search.html", error=error)
    
    allowed_min = datetime(2000, 1, 1)
    allowed_max = datetime(2025, 1, 1)
    if date_min_obj < allowed_min or date_max_obj > allowed_max:
        error = "Release dates must be between 2000-01-01 and 2025-01-01."
        return render_template("search.html", error=error)
    
    query = GAME_SELECT + " WHERE games.release_date >= ? AND games.release_date <= ?"
    params = [date_min, date_max]
    conn = get_db_connection()
    results = conn.execute(query, tuple(params)).fetchall()
    conn.close()
    return render_template("search_results.html", results=results, search_type="Release Date", search_value=f"{date_min} to {date_max}")

@app.route('/search_by_age', methods=["POST"])
def search_by_age():
    age_rating = request.form.get("age_rating", "").strip().upper()  # Convert input to uppercase
    allowed_age_ratings = ["G", "PG", "M", "R13", "R16", "R18"]
    if age_rating not in allowed_age_ratings:
        error = "Invalid age rating. Valid options are: " + ", ".join(allowed_age_ratings) + "."
        return render_template("search.html", error=error)
    
    query = GAME_SELECT + " WHERE age_ratings.rating = ?"
    params = [age_rating]
    conn = get_db_connection()
    results = conn.execute(query, tuple(params)).fetchall()
    conn.close()
    return render_template("search_results.html", results=results, search_type="Age Rating", search_value=age_rating)

@app.route("/game/<int:game_id>")
def game_detail(game_id):
    conn = get_db_connection()
    game = conn.execute(GAME_SELECT + " WHERE games.game_id = ?", (game_id,)).fetchone()
    conn.close()
    if game is None:
        return "Game not found", 404
    return render_template("game_detail.html", game=game)

@app.route("/random")
def random_game():
    conn = get_db_connection()
    games = conn.execute("SELECT game_id FROM games").fetchall()
    conn.close()
    if not games:
        return "No games in database", 404
    random_id = random.choice(games)["game_id"]
    return redirect(url_for("game_detail", game_id=random_id))

if __name__ == '__main__':
    app.run(debug=True)
