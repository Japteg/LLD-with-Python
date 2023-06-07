import abc


class BoardServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialize_board(self, snakes, ladders, players, size=100):
        pass

    @abc.abstractmethod
    def update_player_piece(self, player, dice_throw):
        pass
