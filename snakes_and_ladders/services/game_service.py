from typing import List
from collections import deque
from .game_service_interface import GameServiceInterface
from models.player import Player
from models.snake import Snake
from models.ladder import Ladder
from services.board_service import BoardService
from services.dice_service import DiceService
from services.player_service import PlayerService


class GameService(GameServiceInterface):

    def __init__(self):
        self.player_queue = None
        self.board_service = None
        self.best_position_remaining = 1
        self.dice_service = DiceService(1)

    def initialize_game(self, players: List[Player], snakes: List[Snake],
                        ladders: List[Ladder]):
        self.board_service = BoardService()
        self.board_service.initialize_board(snakes, ladders, players)
        self.player_queue = deque(players)

    def play(self):
        while len(self.player_queue) > 1:
            player = self.player_queue.popleft()
            PlayerService().take_turn(player, self.board_service, self.dice_service)
            if self.is_winner(player):
                print('***************************')
                print(f'{player.get_name()} has won: {self.best_position_remaining}')
                print('***************************')
                self.best_position_remaining += 1
            else:
                self.player_queue.append(player)
        last_player = self.player_queue.popleft()
        print(f'{last_player.get_name()} came last!!!')

    def is_winner(self, player):
        return self.board_service.check_winner(player)
