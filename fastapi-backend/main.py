#Fast API Backend

from fastapi import FastAPI

app = FastAPI()

from data import Players, Games

# base route
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Games

@app.get("/games")
async def games():
    # Return all games
    return {"games": Games.games}

@app.get("/game")
async def games(game_id: int, q: str | None = None):
    # Return a game
    return {"game_id": game_id, "q": q, "result": "game info"}

@app.post("/game/new")
async def game_create(player_id: int, q: str | None = None):
    # Create a new game
    # Return game
    return {"game_id": "game_id", "result": "new game created by" + player_id}
    
@app.post("/game/update")
async def game_update(game_id: int, q: str | None = None):
    # Determine if player or bot has won game
    # Handle game win or continue game
    return {"game_id": game_id, "q": q, "result": "update game"}

@app.post("/game/result")
async def game_result(game_id: int, q: str | None = None):
    # Mark result of game
    # Update player record
    return  {"game_id": game_id, "q": q, "result": "game result"}

# Players

@app.get("/players")
async def get_players():
    # Return all players
    return {"players": Players.players}

@app.get("/player")
async def retrieve_player(player_id: int, q: str | None = None):
    # Return a player
    return {"player_id": player_id, "q": q, "result": "player info"}

# next((player for player in players if player.id == player_id))

@app.post("/player/new")
async def player_create(player_id: int, q: str | None = None):
    # Create a new player
    # Return game
    return {"player_id": "player", "result": "new player created"}

@app.get("/player/move")
async def player_move(game_id: int, q: str | None = None):
    # Record player's move
    # Check if player has won game
    # Return game state
    return {"item_id": game_id, "q": q}

app.get("/player/forfeit")
async def forfeit_game(game_id: int, q: str | None = None):
    # Mark bot as winner
    # Return confirmation
    return {"game_id": game_id, "result": "player forfeits, bot wins"}


# Bots

@app.get("/bot/move")
async def bot_move(game_id: int, q: str | None = None):
    # Determine which bot is playing
    # Bot makes move
    # Check if bot has won game
    # Return game state
    return {"item_id": game_id, "q": q}