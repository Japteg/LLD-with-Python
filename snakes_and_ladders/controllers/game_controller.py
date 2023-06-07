from typing import List
from models.player import Player
from models.snake import Snake
from models.ladder import Ladder
from services.game_service import GameService


class GameController:

    def __init__(self):
        self.game_service = GameService()

    def play_game(self, players: List[Player], snakes: List[Snake],
                  ladders: List[Ladder]):
        self.game_service.initialize_game(players, snakes, ladders)
        self.game_service.play()
