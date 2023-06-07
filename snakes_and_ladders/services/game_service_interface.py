import abc
from typing import List
from models.player import Player
from models.snake import Snake
from models.ladder import Ladder


class GameServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialize_game(self, players: List[Player], snakes: List[Snake],
                        ladders: List[Ladder]):
        pass

    @abc.abstractmethod
    def play(self):
        pass
