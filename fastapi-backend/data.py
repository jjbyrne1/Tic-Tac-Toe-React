# Temporary data added for testing

class Games():

    # List of games
    games = []

    # Create a new game for both player and bot
    def new_game(self, player_id, bot_id):
        game_id = self.games.__len__() + 1
        self.games.append(
            {
                "id": game_id,
                "player": player_id,
                "bot": bot_id,
                "board": [" "] * 9,
                "gameOver": False,
            }
        )
        return id
    
    # Retrieve game if exists
    def find_game(self, game_id):
        return 1
    
    # Update game with chosen move
    def game_update(self, game_id):
        return 1
    
    # Record result of the game
    def game_result(self, game_id):
        return 1

# Games Dummy Data
Games.new_game(Games,0,0)
Games.new_game(Games,1,0)
Games.new_game(Games,2,1)

class Players():

    # List of players
    players = []

    # Create a new player
    def new_player(self, firstName):
        player_id = self.players.__len__() + 1
        self.players.append(
            {
                "id": player_id,
                "firstName": firstName,
                "wins": 0,
                "losses": 0,
                "ratioWL": 0.0,
                "botsPlayed": [0,0],
            }
        )
        return id
    
    # Return a player
    def get_player(self, player_id):
        return 1
    
    def player_make_move(self, player_id, game_id):
        return 1
    
    def player_forfeit_game(self, player_id, game_id):
        return 1

# Players Dummy Data
Players.new_player(Players,'Jason')
Players.new_player(Players,'Bob')
Players.new_player(Players,'Ana')

class Bots():

    # List of bots
    bots = []

    def bot_make_move(self, game_id, bot_id):
        return 1