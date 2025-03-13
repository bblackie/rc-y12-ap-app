import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('games.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    games = conn.execute("""
        SELECT games.id, games.title, games.release_year, games.metacritic_score,
               genres.name AS genre, 
               publishers.name AS publisher, 
               developers.name AS developer
        FROM games
        JOIN genres ON games.genre_id = genres.id
        JOIN publishers ON games.publisher_id = publishers.id
        JOIN developers ON games.developer_id = developers.id
        ORDER BY metacritic_score DESC  -- ✅ Sort games by score
    """).fetchall()
    conn.close()
    return render_template("iteration_proof.html", games=games)

@app.route("/game/<int:game_id>")
def game_page(game_id):
    conn = get_db_connection()
    game = conn.execute("""
        SELECT games.id, games.title, games.release_year, games.description, games.metacritic_score,
               genres.name AS genre, 
               publishers.name AS publisher, 
               developers.name AS developer
        FROM games
        JOIN genres ON games.genre_id = genres.id
        JOIN publishers ON games.publisher_id = publishers.id
        JOIN developers ON games.developer_id = developers.id
        WHERE games.id = ?
    """, (game_id,)).fetchone()

    platforms = conn.execute("""
        SELECT platforms.name 
        FROM game_platforms
        JOIN platforms ON game_platforms.platform_id = platforms.id
        WHERE game_platforms.game_id = ?
    """, (game_id,)).fetchall()
    conn.close()

    return render_template("game_detail.html", game=game, platforms=platforms)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").lower()
    conn = get_db_connection()
    games = conn.execute("""
        SELECT games.id, games.title, games.release_year, games.metacritic_score,
               genres.name AS genre 
        FROM games
        JOIN genres ON games.genre_id = genres.id
        WHERE LOWER(games.title) LIKE ? OR LOWER(genres.name) LIKE ?
        ORDER BY metacritic_score DESC
    """, ('%' + query + '%', '%' + query + '%')).fetchall()
    conn.close()
    return jsonify([dict(game) for game in games])

if __name__ == "__main__":
    app.run(debug=True)
