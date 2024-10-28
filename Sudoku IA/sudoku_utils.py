import numpy as np
import json

def save_game(board, solution):
    game_data = {
        'board': board.tolist(),
        'solution': solution.tolist()
    }
    with open('saved_game.json', 'w') as f:
        json.dump(game_data, f)

def load_game():
    try:
        with open('saved_game.json', 'r') as f:
            game_data = json.load(f)
            return np.array(game_data['board']), np.array(game_data['solution'])
    except FileNotFoundError:
        return None, None
