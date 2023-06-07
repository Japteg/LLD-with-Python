import abc
from .board_service import BoardService
from .dice_service import DiceService
from models.player import Player


class PlayerServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def take_turn(self, player: Player, board_service: BoardService,
                  dice_service: DiceService):
        """
        roll dice and move piece
        """
        pass
