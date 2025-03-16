from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__)
DATABASE = 'games.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable column access by name
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    games = conn.execute("SELECT * FROM games").fetchall()
    conn.close()
    return render_template("index.html", all_games=games)

@app.route('/search', methods=["GET", "POST"])
def search():
    conn = get_db_connection()
    if request.method == "POST":
        # Retrieve search inputs
        search_term = request.form.get("search_term", "").strip()
        score_min = request.form.get("score-min", "").strip()
        score_max = request.form.get("score-max", "").strip()
        date_min = request.form.get("date-min", "").strip()
        date_max = request.form.get("date-max", "").strip()
        nz_ratings = request.form.getlist("nz_rating")  # May be empty list
        
        # If nothing is entered in any field (except the sliders which default to 0 and 100),
        # show an error message instead of returning all games.
        if not search_term and not date_min and not date_max and not nz_ratings:
            error = "You must enter something in the search boxes to proceed."
            conn.close()
            return render_template("search.html", error=error, searched=True, results=[], all_games=[])

        query = "SELECT * FROM games WHERE 1=1"
        params = []
        
        # Wildcard, case‑insensitive search across title, developer, and publisher
        if search_term:
            query += " AND (title LIKE ? COLLATE NOCASE OR developer LIKE ? COLLATE NOCASE OR publisher LIKE ? COLLATE NOCASE)"
            wildcard = f"%{search_term}%"
            params.extend([wildcard, wildcard, wildcard])
        if score_min:
            query += " AND metacritic_score >= ?"
            params.append(score_min)
        if score_max:
            query += " AND metacritic_score <= ?"
            params.append(score_max)
        if date_min:
            query += " AND release_date >= ?"
            params.append(date_min)
        if date_max:
            query += " AND release_date <= ?"
            params.append(date_max)
        if nz_ratings:
            placeholders = ','.join('?' * len(nz_ratings))
            query += f" AND nz_age_rating IN ({placeholders})"
            params.extend(nz_ratings)

        results = conn.execute(query, tuple(params)).fetchall()
        # When searching, we don't display the default All Games list.
        conn.close()
        return render_template("search.html", searched=True, results=results, all_games=[])
    else:
        # When GET, show the default All Games list (4x5 grid)
        all_games = conn.execute("SELECT * FROM games").fetchall()
        conn.close()
        return render_template("search.html", searched=False, all_games=all_games, results=[])

@app.route("/game/<int:game_id>")
def game_detail(game_id):
    conn = get_db_connection()
    game = conn.execute("SELECT * FROM games WHERE id = ?", (game_id,)).fetchone()
    conn.close()
    if game is None:
        return "Game not found", 404
    return render_template("game_detail.html", game=game)

@app.route("/random")
def random_game():
    conn = get_db_connection()
    games = conn.execute("SELECT id FROM games").fetchall()
    conn.close()
    if not games:
        return "No games in database", 404
    random_id = random.choice(games)["id"]
    return redirect(url_for("game_detail", game_id=random_id))

if __name__ == '__main__':
    app.run(debug=True)
