from flask import Flask, render_template

app = Flask(__name__)

# Game Data (Using File Names)
games = [
    {"route": "zelda", "title": "The Legend of Zelda: Breath of the Wild", "publisher": "Nintendo", "developer": "Nintendo"},
    {"route": "elden_ring", "title": "Elden Ring", "publisher": "Bandai Namco Entertainment", "developer": "FromSoftware"},
    {"route": "witcher3", "title": "The Witcher 3: Wild Hunt", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"route": "gta5", "title": "Grand Theft Auto V", "publisher": "Rockstar Games", "developer": "Rockstar North"},
    {"route": "rdr2", "title": "Red Dead Redemption 2", "publisher": "Rockstar Games", "developer": "Rockstar Games"},
    {"route": "cyberpunk", "title": "Cyberpunk 2077", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"route": "minecraft", "title": "Minecraft", "publisher": "Mojang", "developer": "Mojang"},
    {"route": "fortnite", "title": "Fortnite", "publisher": "Epic Games", "developer": "Epic Games"},
    {"route": "god_of_war", "title": "God of War (2018)", "publisher": "Sony Interactive Entertainment", "developer": "Santa Monica Studio"},
    {"route": "mario", "title": "Super Mario Odyssey", "publisher": "Nintendo", "developer": "Nintendo"}
]

@app.route("/")
def index():
    return render_template("index.html", games=games)

@app.route("/game/<game_name>")
def game_page(game_name):
    game = next((g for g in games if g["route"] == game_name), None)
    if game:
        return render_template(f"{game_name}.html", game=game)
    return "Game not found", 404

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

# Game Data (Using File Names)
games = [
    {"route": "zelda", "title": "The Legend of Zelda: Breath of the Wild", "publisher": "Nintendo", "developer": "Nintendo"},
    {"route": "elden_ring", "title": "Elden Ring", "publisher": "Bandai Namco Entertainment", "developer": "FromSoftware"},
    {"route": "witcher3", "title": "The Witcher 3: Wild Hunt", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"route": "gta5", "title": "Grand Theft Auto V", "publisher": "Rockstar Games", "developer": "Rockstar North"},
    {"route": "rdr2", "title": "Red Dead Redemption 2", "publisher": "Rockstar Games", "developer": "Rockstar Games"},
    {"route": "cyberpunk", "title": "Cyberpunk 2077", "publisher": "CD Projekt", "developer": "CD Projekt Red"},
    {"route": "minecraft", "title": "Minecraft", "publisher": "Mojang", "developer": "Mojang"},
    {"route": "fortnite", "title": "Fortnite", "publisher": "Epic Games", "developer": "Epic Games"},
    {"route": "god_of_war", "title": "God of War (2018)", "publisher": "Sony Interactive Entertainment", "developer": "Santa Monica Studio"},
    {"route": "mario", "title": "Super Mario Odyssey", "publisher": "Nintendo", "developer": "Nintendo"}
]

@app.route("/")
def index():
    return render_template("index.html", games=games)

@app.route("/game/<game_name>")
def game_page(game_name):
    game = next((g for g in games if g["route"] == game_name), None)
    if game:
        return render_template(f"{game_name}.html", game=game)
    return "Game not found", 404

if __name__ == "__main__":
    app.run(debug=True)



