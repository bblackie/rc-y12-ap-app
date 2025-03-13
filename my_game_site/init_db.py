# init_db.py

import sqlite3  # Import the SQLite3 module for database operations

def create_and_populate_db():
    """
    Connects to the SQLite database (or creates it if it doesn't exist),
    creates the 'games' table, and inserts 10 game records.
    """
    # Connect to the SQLite database file named 'games.db'
    connection = sqlite3.connect('games.db')
    # Set row_factory to sqlite3.Row so we can access columns by name
    cursor = connection.cursor()

    # Drop the table if it already exists to start fresh
    cursor.execute("DROP TABLE IF EXISTS games")

    # Create the 'games' table with the following fields:
    cursor.execute("""
        CREATE TABLE games (
            id INTEGER PRIMARY KEY,              -- Unique identifier for each game
            title TEXT NOT NULL,                 -- Title of the game
            genre TEXT NOT NULL,                 -- Genre of the game
            release_date TEXT NOT NULL,          -- Release date as a text (YYYY-MM-DD)
            developer TEXT NOT NULL,             -- Developer name
            publisher TEXT NOT NULL,             -- Publisher name
            metacritic_score INTEGER NOT NULL    -- Metacritic score as an integer
        );
    """)

    # Define a list of tuples representing each game record
    games_data = [
        (1, 'The Legend of Zelda: Breath of the Wild', 'Action-adventure', '2017-03-03', 'Nintendo', 'Nintendo', 97),
        (2, 'Elden Ring', 'Action RPG', '2022-02-25', 'FromSoftware', 'Bandai Namco Entertainment', 94),
        (3, 'The Witcher 3: Wild Hunt', 'RPG', '2015-05-19', 'CD Projekt Red', 'CD Projekt', 93),
        (4, 'Grand Theft Auto V', 'Open-world, Action-adventure', '2013-09-17', 'Rockstar North', 'Rockstar Games', 97),
        (5, 'Red Dead Redemption 2', 'Action-adventure', '2018-10-26', 'Rockstar Games', 'Rockstar Games', 97),
        (6, 'Fortnite', 'Battle Royale / Sandbox', '2017-09-26', 'Epic Games', 'Epic Games', 81),  # Fortnite replaces PUBG
        (7, 'Minecraft', 'Sandbox, Survival', '2011-11-18', 'Mojang', 'Mojang', 93),
        (8, 'God of War', 'Action', '2018-04-20', 'Santa Monica Studio', 'Sony Interactive Entertainment', 94),
        (9, 'Overwatch', 'First-person shooter', '2016-05-24', 'Blizzard Entertainment', 'Blizzard Entertainment', 91),
        (10, 'Call of Duty: Modern Warfare', 'First-person shooter', '2019-10-25', 'Infinity Ward', 'Activision', 80)
    ]

    # Insert all game records into the 'games' table
    cursor.executemany("""
        INSERT INTO games (id, title, genre, release_date, developer, publisher, metacritic_score)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """, games_data)

    # Commit the changes to the database and close the connection
    connection.commit()
    connection.close()
    print("Database created and populated successfully with 10 games.")

# When the script is run directly, call the function to create and populate the database.
if __name__ == '__main__':
    create_and_populate_db()
