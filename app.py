from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load game data from JSON
with open("games_data.json", "r") as f:
    games = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", games=games)

@app.route("/game/<int:game_id>")
def game_page(game_id):
    game = next((game for game in games if game["Game_Id"] == game_id), None)
    if game:
        return render_template("game_page.html", game=game)
    return "Game not found", 404

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    platform = request.args.get("platform", "").lower()
    
    filtered_games = [game for game in games if query in game["Title"].lower() or query in game["Publisher"].lower()]
    
    if platform:
        filtered_games = [game for game in filtered_games if platform in game["Platforms"].lower()]
    
    return jsonify(filtered_games)

if __name__ == "__main__":
    app.run(debug=True)
