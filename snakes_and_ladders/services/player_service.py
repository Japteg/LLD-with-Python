from .player_service_interface import PlayerServiceInterface
from .board_service import BoardService
from .dice_service import DiceService


class PlayerService(PlayerServiceInterface):

    def take_turn(self, player, board_service: BoardService, dice_service: DiceService):
        dice_throw = dice_service.roll()
        board_service.update_player_piece(player, dice_throw)
