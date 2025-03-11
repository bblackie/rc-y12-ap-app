from flask import Flask, render_template

app = Flask(__name__)

# Game Data (Titles, Publishers, Developers)
games = [
    {"title": "The Legend of Zelda: Breath of the Wild", "publisher": "Nintendo", "developer": "Nintendo"},
    {"title": "Elden Ring", "publisher": "Bandai Namco Entertainment", "developer": "FromSoftware"},
    {"title": "The Witcher 3: Wild Hunt", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"title": "Grand Theft Auto V", "publisher": "Rockstar Games", "developer": "Rockstar North"},
    {"title": "Red Dead Redemption 2", "publisher": "Rockstar Games", "developer": "Rockstar Games"},
    {"title": "Cyberpunk 2077", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"title": "Minecraft", "publisher": "Mojang", "developer": "Mojang"},
    {"title": "Fortnite", "publisher": "Epic Games", "developer": "Epic Games"},
    {"title": "God of War (2018)", "publisher": "Sony Interactive Entertainment", "developer": "Santa Monica Studio"},
    {"title": "Super Mario Odyssey", "publisher": "Nintendo", "developer": "Nintendo"}
]

# Unique & sorted lists for publishers and developers
publishers = sorted(set(game["publisher"] for game in games))
developers = sorted(set(game["developer"] for game in games))

@app.route("/")
def index():
    return render_template("index.html", games=games, publishers=publishers, developers=developers)

@app.route("/game/<int:game_id>")
def game_page(game_id):
    if 1 <= game_id <= len(games):
        return render_template("game_page.html", game=games[game_id - 1])
    return "Game not found", 404

if __name__ == "__main__":
    app.run(debug=True)
