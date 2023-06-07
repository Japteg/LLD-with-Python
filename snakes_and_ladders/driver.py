import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from parser import InputParser
from controllers.game_controller import GameController

# Read input from file
entities = InputParser('sample_input.txt').parse()
players = entities.get('players', [])
ladders = entities.get('ladders', [])
snakes = entities.get('snakes', [])

game_controller = GameController()
game_controller.play_game(players, snakes, ladders)
