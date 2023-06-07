class GameBoard:

    def __init__(self, size=100):
        self.size = size
        self.snakes = {}  # map of snake head position and snake object
        self.ladders = {}  # map of ladder start position and ladder object
        self.player_pieces = {}  # map of player and its current position on board

    def get_size(self):
        return self.size

    def get_snakes(self):
        return self.snakes

    def get_ladders(self):
        return self.ladders

    def get_player_pieces(self):
        return self.player_pieces

    def set_size(self, size):
        self.size = size

    def set_snakes(self, snakes):
        self.snakes = snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def set_player_pieces(self, player_pieces):
        self.player_pieces = player_pieces
