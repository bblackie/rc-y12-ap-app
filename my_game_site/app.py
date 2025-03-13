# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3  # For database operations
import random   # To select a random game

# Create the Flask app
app = Flask(__name__)

# Database filename (SQLite)
DATABASE = 'games.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        conn (sqlite3.Connection): The database connection object.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

@app.route('/')
def home():
    """
    Home page route.
    Fetches all games from the database and renders the home page template.
    The home page includes a massive, centered search bar and a list of all games.
    """
    conn = get_db_connection()  # Connect to the database
    games = conn.execute('SELECT * FROM games').fetchall()  # Retrieve all game records
    conn.close()  # Close the connection
    return render_template('index.html', games=games)  # Render the index template

@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Search page route.
    Handles both GET and POST requests.
    GET: Renders the search form along with a static list of all games.
    POST: Processes the search form, queries the database based on user input,
          and displays the results along with the full list of games.
    """
    conn = get_db_connection()  # Connect to the database

    if request.method == 'POST':
        # Retrieve search parameters from the form
        developer = request.form.get('developer', '')
        publisher = request.form.get('publisher', '')
        title = request.form.get('title', '')
        score_min = request.form.get('score-min', '')
        score_max = request.form.get('score-max', '')
        date_min = request.form.get('date-min', '')
        date_max = request.form.get('date-max', '')

        # Build the SQL query with dynamic filtering based on input
        query = "SELECT * FROM games WHERE 1=1"  # Base query (always true)
        params = []  # Parameters list to prevent SQL injection

        # Add filters if the corresponding field is provided
        if developer:
            query += " AND developer LIKE ?"
            params.append(f"%{developer}%")
        if publisher:
            query += " AND publisher LIKE ?"
            params.append(f"%{publisher}%")
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
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

        # Execute the query with the provided parameters
        results = conn.execute(query, tuple(params)).fetchall()
        # Also fetch all games for a static list display on the search page
        all_games = conn.execute("SELECT * FROM games").fetchall()
        conn.close()  # Close the connection

        # Render the search template with search results and the full games list
        return render_template('search.html', results=results, searched=True, all_games=all_games)
    else:
        # For GET requests, just fetch all games for the static list display
        all_games = conn.execute("SELECT * FROM games").fetchall()
        conn.close()  # Close the connection
        return render_template('search.html', results=None, searched=False, all_games=all_games)

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    """
    Game detail page route.
    Fetches details for a specific game based on the game_id.
    If the game is not found, returns a 404 error.
    """
    conn = get_db_connection()  # Connect to the database
    game = conn.execute('SELECT * FROM games WHERE id = ?', (game_id,)).fetchone()  # Fetch one record by id
    conn.close()  # Close the connection

    # If no game is found, return a 404 error
    if game is None:
        return "Game not found", 404

    # Render the game detail template with the game data
    return render_template('game_detail.html', game=game)

@app.route('/random')
def random_game():
    """
    Random game route.
    Selects a random game from the database and redirects to its detail page.
    """
    conn = get_db_connection()  # Connect to the database
    games = conn.execute('SELECT id FROM games').fetchall()  # Fetch only the game IDs
    conn.close()  # Close the connection

    # Check if there are any games in the database
    if not games:
        return "No games in database", 404

    # Randomly choose a game id from the list of games
    random_id = random.choice(games)['id']
    # Redirect to the game detail page for the randomly selected game
    return redirect(url_for('game_detail', game_id=random_id))

# Run the Flask app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
